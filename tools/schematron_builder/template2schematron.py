#!/usr/bin/env python3
"""
template2schematron.py

Uses lxml if available for robust comment handling; falls back to xml.etree.ElementTree.

Usage:
    python template2schematron.py <template_file> <xsd_file> <input_folder> <output_file>
"""
import sys
import os
import re

# Prefer lxml if available
try:
    import lxml.etree as LET
    from lxml.etree import Element as LET_Element, Comment as LET_Comment
    HAS_LXML = True
except Exception:
    LET = None
    HAS_LXML = False
    import xml.etree.ElementTree as ET
    from xml.etree.ElementTree import Element as ET_Element, Comment as ET_Comment

# Markers and regexes
START_MARKER = "ch-start"
END_MARKER = "ch-stop"
RE_NOTE = re.compile(r'\bch-note\s*:\s*(.*)', re.IGNORECASE)
RE_USAGE = re.compile(r'\bch-usage\s*:\s*(\w+)', re.IGNORECASE)
RE_REFERENCED = re.compile(r'\bch-referenced\b', re.IGNORECASE)
RE_REFERENCED_ALT = re.compile(r'\breferenced\b', re.IGNORECASE)
RE_REFERENCED_WITH_ARGS = re.compile(r'\bch-referenced\s*:\s*(.+)', re.IGNORECASE)
RE_ALLOWED_ENUMS = re.compile(r'\bch-allowed-enums\s*:\s*(.+)', re.IGNORECASE)

# Verbose debug toggle
VERBOSE = False

def usage():
    print("Usage: python template2schematron.py <template_file> <xsd_file> <input_folder> <output_file>")
    sys.exit(2)

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    d = os.path.dirname(path)
    if d and not os.path.exists(d):
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def indent_et(elem, level=0):
    """In-place pretty‑print indent for xml.etree.ElementTree elements."""
    i = "\n" + ("  " * level)
    # if element has no children, leave text as-is (but ensure no stray whitespace)
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent_et(child, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if not elem.tail or not elem.tail.strip():
            elem.tail = i


def extract_regions(text, start_marker=START_MARKER, end_marker=END_MARKER):
    lines = text.splitlines(keepends=True)
    results, collecting, buf = [], False, []
    for line in lines:
        if not collecting and start_marker in line:
            collecting = True
            buf.append(line)
            continue
        if collecting:
            buf.append(line)
            if end_marker in line:
                results.append(''.join(buf))
                buf = []
                collecting = False
    if collecting and buf:
        results.append(''.join(buf))
    return results

def wrap_fragment(fragment):
    # Use XML declaration and artificial root
    return '<?xml version="1.0" encoding="utf-8"?><__root__>' + fragment + '</__root__>'

def parse_usage_and_notes_from_comments(comment_text):
    notes = RE_NOTE.findall(comment_text)
    usages = RE_USAGE.findall(comment_text)

    referenced_names = []
    args_match = RE_REFERENCED_WITH_ARGS.search(comment_text)
    if args_match:
        vals = args_match.group(1).strip()
        referenced_names = [v for v in re.split(r'\s+', vals) if v != '']
    else:
        if RE_REFERENCED.search(comment_text) or RE_REFERENCED_ALT.search(comment_text):
            referenced_names = ['__DEFAULT__']

    allowed_match = RE_ALLOWED_ENUMS.search(comment_text)
    allowed = []
    if allowed_match:
        vals = allowed_match.group(1).strip()
        allowed = [v for v in re.split(r'\s+', vals) if v != '']
    return {
        'notes': [n.strip() for n in notes] if notes else [],
        'usages': [u.strip().lower() for u in usages] if usages else [],
        'referenced_names': referenced_names,
        'allowed_enums': allowed
    }

def local_name(tag):
    if tag is None:
        return ''
    # strip namespace if present
    m = re.match(r'\{.*\}(.*)', tag)
    return m.group(1) if m else tag

# Node utilities abstracting lxml vs ET
def parse_xml_fragment(fragment_text):
    """Parse wrapped fragment text and return a root element (lxml or ET)."""
    if HAS_LXML:
        return LET.fromstring(fragment_text.encode('utf-8'))
    else:
        return ET.fromstring(fragment_text)

def iter_children(node):
    """Return list of direct children in order."""
    if HAS_LXML:
        return list(node)
    else:
        return list(node)

def is_comment(node):
    """Detect comment nodes for current parser."""
    if HAS_LXML:
        return isinstance(node, LET._Comment)
    else:
        # ElementTree: node.tag is ET.Comment in many builds or tag == 'comment'
        try:
            if node.tag is ET.Comment:
                return True
        except Exception:
            pass
        try:
            if isinstance(node.tag, str) and node.tag.lower() == 'comment':
                return True
        except Exception:
            pass
        return False

# Schematron builder (using ET to build output; this is independent from parsing library)
import xml.etree.ElementTree as OUT_ET
from xml.etree.ElementTree import Element as OUT_Element, SubElement as OUT_SubElement

class SchematronBuilder:
    def __init__(self, xsd_path):
        self.xsd_path = xsd_path
        self.schema = OUT_Element('schema', attrib={'xmlns': 'http://purl.oclc.org/dsdl/schematron'})
        title = OUT_SubElement(self.schema, 'title')
        title.text = 'Generated schematron from template'
        self.pattern = OUT_SubElement(self.schema, 'pattern', attrib={'id': 'p1'})
        self.processed_files = set()
        self.rules_created = 0

    def add_comment_to_rule(self, parent, text):
        parent.append(OUT_ET.Comment(' ' + text + ' '))

    def add_rule_presence(self, context_xpath, element_name, note_text=None):
        rule = OUT_SubElement(self.pattern, 'rule', attrib={'context': context_xpath})
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        OUT_SubElement(rule, 'assert', attrib={'test': f'count({element_name}) &gt; 0'}).text = f'{element_name} must be present'
        self.rules_created += 1

    def add_rule_absence(self, context_xpath, element_name, note_text=None):
        rule = OUT_SubElement(self.pattern, 'rule', attrib={'context': context_xpath})
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        OUT_SubElement(rule, 'assert', attrib={'test': f'count({element_name}) = 0'}).text = f'{element_name} must NOT be present'
        self.rules_created += 1

    def add_rule_allowed_enums(self, context_xpath, element_name, allowed_list, note_text=None):
        if not allowed_list:
            return
        ors = ' or '.join([f"{element_name} = '{val}'" for val in allowed_list])
        rule = OUT_SubElement(self.pattern, 'rule', attrib={'context': context_xpath})
        if note_text:
            self.add_comment_to_rule(rule, note_text)
        OUT_SubElement(rule, 'assert', attrib={'test': ors}).text = f'{element_name} must be one of: {" ".join(allowed_list)}'
        self.rules_created += 1

    def tostring(self):
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + OUT_ET.tostring(self.schema, encoding='unicode')

def find_files_for_candidate(input_folder, candidate_filename):
    matches = []
    for root, dirs, files in os.walk(input_folder):
        if candidate_filename in files:
            matches.append(os.path.join(root, candidate_filename))
    return matches

def _process_fragment_root(rootfrag, parent_tag_local, builder, input_folder):
    nodes = iter_children(rootfrag)
    for node in nodes:
        if is_comment(node):
            if VERBOSE:
                print("Fragment comment:", repr(node.text if HAS_LXML else node.text))
            ctext = (node.text or '').strip() if (HAS_LXML or getattr(node, 'text', None) is not None) else ''
            parsed = parse_usage_and_notes_from_comments(ctext)
            notes = parsed['notes']; usages = parsed['usages']; referenced_names = parsed['referenced_names']; allowed_enums = parsed['allowed_enums']
            note_text = '; '.join(notes) if notes else None
            if any(u == 'forbidden' for u in usages):
                builder.add_rule_absence(f'.//{parent_tag_local}' if parent_tag_local else '.', parent_tag_local or '.', note_text=note_text)
            if any(u == 'mandatory' for u in usages):
                builder.add_rule_presence(f'.//{parent_tag_local}' if parent_tag_local else '.', parent_tag_local or '.', note_text=note_text)
            if allowed_enums:
                builder.add_rule_allowed_enums(f'.//{parent_tag_local}' if parent_tag_local else '.', parent_tag_local or '.', allowed_enums, note_text=note_text)
            if referenced_names:
                tokens = []
                if all(t == '__DEFAULT__' for t in referenced_names):
                    tokens = ['__DEFAULT__']
                else:
                    for t in referenced_names:
                        if t != '__DEFAULT__':
                            tokens.append(t)
                    if '__DEFAULT__' in referenced_names:
                        tokens.append('__DEFAULT__')
                for token in tokens:
                    candidates = []
                    if token == '__DEFAULT__':
                        if parent_tag_local:
                            candidates.append(f'{parent_tag_local}.xml')
                    else:
                        candidates.append(token if token.lower().endswith('.xml') else f'{token}.xml')
                    for candidate in candidates:
                        for found_path in find_files_for_candidate(input_folder, candidate):
                            ab = os.path.abspath(found_path)
                            if ab in builder.processed_files:
                                continue
                            builder.processed_files.add(ab)
                            try:
                                txt = read_file(found_path)
                            except Exception as e:
                                print(f'Warning: cannot read referenced file {found_path}: {e}', file=sys.stderr)
                                continue
                            regions = extract_regions(txt)
                            if not regions:
                                regions = [txt]
                            for r in regions:
                                wrapped = wrap_fragment(r)
                                try:
                                    subfrag = parse_xml_fragment(wrapped)
                                except Exception as e:
                                    print(f'Warning: parse error in referenced file {found_path}: {e}', file=sys.stderr)
                                    continue
                                _process_fragment_root(subfrag, parent_tag_local, builder, input_folder)
        else:
            # element node - call element processing
            process_element_tree(node, builder, context_xpath=f'.//{parent_tag_local}' if parent_tag_local else '.', input_folder=input_folder, ancestor_forbidden=False)

def process_element_tree(elem, builder, context_xpath='.', input_folder='.', ancestor_forbidden=False):
    if ancestor_forbidden:
        return
    tag_local = local_name(elem.tag if HAS_LXML else elem.tag)
    if VERBOSE:
        print("Processing element:", tag_local, "context:", context_xpath)
    nodes = iter_children(elem)
    child_elements = []
    child_comments = []
    for node in nodes:
        if is_comment(node):
            child_comments.append(node)
        else:
            child_elements.append(node)
    for comment_node in child_comments:
        ctext = (comment_node.text or '').strip() if (HAS_LXML or getattr(comment_node, 'text', None) is not None) else ''
        parsed = parse_usage_and_notes_from_comments(ctext)
        notes = parsed['notes']; usages = parsed['usages']; referenced_names = parsed['referenced_names']; allowed_enums = parsed['allowed_enums']
        note_text = '; '.join(notes) if notes else None
        if any(u == 'forbidden' for u in usages):
            builder.add_rule_absence(context_xpath, tag_local, note_text=note_text)
        if any(u == 'mandatory' for u in usages):
            builder.add_rule_presence(context_xpath, tag_local, note_text=note_text)
        if allowed_enums:
            builder.add_rule_allowed_enums(context_xpath, tag_local, allowed_enums, note_text=note_text)
        if referenced_names:
            tokens = []
            if all(t == '__DEFAULT__' for t in referenced_names):
                tokens = ['__DEFAULT__']
            else:
                for t in referenced_names:
                    if t != '__DEFAULT__':
                        tokens.append(t)
                if '__DEFAULT__' in referenced_names:
                    tokens.append('__DEFAULT__')
            for token in tokens:
                candidates = []
                if token == '__DEFAULT__':
                    candidates.append(f'{tag_local}.xml')
                else:
                    candidates.append(token if token.lower().endswith('.xml') else f'{token}.xml')
                for candidate in candidates:
                    for found_path in find_files_for_candidate(input_folder, candidate):
                        ab = os.path.abspath(found_path)
                        if ab in builder.processed_files:
                            continue
                        builder.processed_files.add(ab)
                        try:
                            txt = read_file(found_path)
                        except Exception as e:
                            print(f'Warning: cannot read referenced file {found_path}: {e}', file=sys.stderr)
                            continue
                        regions = extract_regions(txt)
                        if not regions:
                            regions = [txt]
                        for r in regions:
                            wrapped = wrap_fragment(r)
                            try:
                                rootfrag = parse_xml_fragment(wrapped)
                            except Exception as e:
                                print(f'Warning: parse error in referenced file {found_path}: {e}', file=sys.stderr)
                                continue
                            _process_fragment_root(rootfrag, tag_local, builder, input_folder)
    for child in child_elements:
        process_element_tree(child, builder, context_xpath=f'.//{tag_local}', input_folder=input_folder, ancestor_forbidden=False)

def main(argv):
    if len(argv) != 5:
        usage()
    _, template_path, xsd_path, input_folder, output_path = argv
    if not os.path.isfile(template_path):
        print(f'Error: template file not found: {template_path}', file=sys.stderr)
        sys.exit(1)
    if not os.path.isfile(xsd_path):
        print(f'Warning: xsd file not found: {xsd_path}', file=sys.stderr)
    if not os.path.isdir(input_folder):
        print(f'Warning: input folder not found: {input_folder}', file=sys.stderr)
    txt = read_file(template_path)
    regions = extract_regions(txt)
    if not regions:
        print('Warning: no regions found between markers; attempting to process entire file', file=sys.stderr)
        regions = [txt]
    builder = SchematronBuilder(xsd_path)
    for region in regions:
        wrapped = wrap_fragment(region)
        try:
            root = parse_xml_fragment(wrapped)
        except Exception as e:
            print(f'Error parsing extracted region: {e}', file=sys.stderr)
            continue
        for node in iter_children(root):
            if is_comment(node):
                ctext = (node.text or '').strip() if (HAS_LXML or getattr(node, 'text', None) is not None) else ''
                parsed = parse_usage_and_notes_from_comments(ctext)
                notes = parsed['notes']; usages = parsed['usages']; referenced_names = parsed['referenced_names']; allowed_enums = parsed['allowed_enums']
                note_text = '; '.join(notes) if notes else None
                if any(u == 'forbidden' for u in usages):
                    builder.add_rule_absence('.', '.', note_text=note_text)
                if any(u == 'mandatory' for u in usages):
                    builder.add_rule_presence('.', '.', note_text=note_text)
                if referenced_names:
                    tokens = []
                    if all(t == '__DEFAULT__' for t in referenced_names):
                        tokens = ['__DEFAULT__']
                    else:
                        for t in referenced_names:
                            if t != '__DEFAULT__':
                                tokens.append(t)
                        if '__DEFAULT__' in referenced_names:
                            tokens.append('__DEFAULT__')
                    for token in tokens:
                        if token == '__DEFAULT__':
                            continue
                        candidates = [token if token.lower().endswith('.xml') else f'{token}.xml']
                        for candidate in candidates:
                            for found_path in find_files_for_candidate(input_folder, candidate):
                                ab = os.path.abspath(found_path)
                                if ab in builder.processed_files:
                                    continue
                                builder.processed_files.add(ab)
                                try:
                                    txt = read_file(found_path)
                                except Exception as e:
                                    print(f'Warning: cannot read referenced file {found_path}: {e}', file=sys.stderr)
                                    continue
                                regions = extract_regions(txt)
                                if not regions:
                                    regions = [txt]
                                for r in regions:
                                    wrapped_r = wrap_fragment(r)
                                    try:
                                        rootfrag = parse_xml_fragment(wrapped_r)
                                    except Exception as e:
                                        print(f'Warning: parse error in referenced file {found_path}: {e}', file=sys.stderr)
                                        continue
                                    _process_fragment_root(rootfrag, None, builder, input_folder)
            else:
                process_element_tree(node, builder, context_xpath='.', input_folder=input_folder, ancestor_forbidden=False)
    out = builder.tostring()
    write_file(output_path, out)
    print(f'Wrote schematron to {output_path}. Rules created: {builder.rules_created}')

if __name__ == '__main__':
    main(sys.argv)

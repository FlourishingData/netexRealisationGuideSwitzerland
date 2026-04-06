#!/usr/bin/env python3
"""
Markdown Builder for NeTEx templates
Extracts documentation from annotated XML templates and generates markdown tables
with type information from XSD schemas.
"""

import os
import sys
import argparse
from lxml import etree
from collections import defaultdict
import re


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Generate markdown documentation from NeTEx templates')
    parser.add_argument('-i', '--input', required=True, help='Input folder containing XML templates')
    parser.add_argument('-o', '--output', required=True, help='Output folder for markdown files')
    parser.add_argument('-x', '--xsd', required=True, help='XSD schema file for type information')
    return parser.parse_args()


def load_xsd_type_info(xsd_path):
    """Load type and cardinality information from XSD"""
    try:
        # Ensure the path is absolute
        xsd_path = os.path.abspath(xsd_path)
        print(f"Loading XSD from: {xsd_path}")
        print(f"XSD exists: {os.path.exists(xsd_path)}")
        xsd_doc = etree.parse(xsd_path)
        xsd_root = xsd_doc.getroot()
        
        # Namespaces
        ns = {'xs': 'http://www.w3.org/2001/XMLSchema'}
        
        type_info = {}
        
        # Extract complex types
        for complex_type in xsd_root.findall('.//xs:complexType', namespaces=ns):
            name = complex_type.get('name')
            if name:
                type_info[name] = {'type': 'complex', 'elements': {}}
                
                # Extract elements within this complex type
                for element in complex_type.findall('.//xs:element', namespaces=ns):
                    elem_name = element.get('name')
                    elem_type = element.get('type')
                    min_occurs = element.get('minOccurs', '1')
                    max_occurs = element.get('maxOccurs', '1')
                    
                    if elem_name:
                        type_info[name]['elements'][elem_name] = {
                            'type': elem_type,
                            'min_occurs': min_occurs,
                            'max_occurs': max_occurs
                        }
        
        # Extract simple types
        for simple_type in xsd_root.findall('.//xs:simpleType', namespaces=ns):
            name = simple_type.get('name')
            if name:
                type_info[name] = {'type': 'simple'}
        
        # Extract top-level elements
        for element in xsd_root.findall('.//xs:element', namespaces=ns):
            name = element.get('name')
            elem_type = element.get('type')
            min_occurs = element.get('minOccurs', '1')
            max_occurs = element.get('maxOccurs', '1')
            
            if name:
                type_info[name] = {
                    'type': elem_type,
                    'min_occurs': min_occurs,
                    'max_occurs': max_occurs,
                    'element_type': 'top_level'
                }
        
        return type_info
    
    except Exception as e:
        print(f"Error loading XSD: {e}")
        return {}


def get_cardinality(min_occurs, max_occurs):
    """Convert min/max occurs to cardinality string"""
    if min_occurs == '0' and max_occurs == '1':
        return '0..1'
    elif min_occurs == '1' and max_occurs == '1':
        return '1..1'
    elif min_occurs == '0' and max_occurs == 'unbounded':
        return '0..*'
    elif min_occurs == '1' and max_occurs == 'unbounded':
        return '1..*'
    else:
        return f"{min_occurs}..{max_occurs}"


def parse_template_file(file_path, xsd_type_info):
    """Parse a single template file and extract documentation"""
    try:
        doc = etree.parse(file_path)
        root = doc.getroot()
        
        # Register namespace if present
        nsmap = root.nsmap
        ns = {}
        if None in nsmap:
            # Default namespace
            default_ns = nsmap[None]
            ns['default'] = default_ns
        
        # Find ch-start and ch-stop comments
        comments = root.xpath('//comment()', namespaces=ns)
        
        start_idx = None
        stop_idx = None
        
        for i, comment in enumerate(comments):
            text = comment.text.strip()
            if 'ch-start:' in text:
                start_idx = i
            elif 'ch-stop:' in text:
                stop_idx = i
                break
        
        if start_idx is None or stop_idx is None:
            print(f"Warning: No ch-start or ch-stop found in {file_path}")
            return None
        
        # Get the elements between start and stop
        elements_data = []
        
        # Find the parent element that contains our comments
        start_comment = comments[start_idx]
        stop_comment = comments[stop_idx]
        
        # Get the common ancestor
        start_parent = start_comment.getparent()
        stop_parent = stop_comment.getparent()
        
        # Find common ancestor
        common_ancestor = start_parent
        while common_ancestor is not None:
            if common_ancestor == stop_parent or stop_parent in common_ancestor.xpath('descendant::*'):
                break
            common_ancestor = common_ancestor.getparent()
        
        if common_ancestor is None:
            common_ancestor = root
        
        # Process elements in the range
        processed_elements = set()
        
        def process_element(element, level=0):
            """Recursively process an element and its children"""
            # Handle namespace properly
            if hasattr(element, 'tag'):
                elem_name = etree.QName(element).localname
            else:
                return  # Skip non-element nodes
            elem_id = element.get('id')
            
            # Skip if already processed (avoid duplicates)
            elem_key = f"{elem_name}_{elem_id}" if elem_id else elem_name
            if elem_key in processed_elements:
                return
            processed_elements.add(elem_key)
            
            # Get comments for this element
            usage = 'ignored'
            note = ''
            notice = ''
            is_referenced = False
            referenced_name = None
            
            # Get comments that are direct children of this element (before any child elements)
            # These are the comments that describe the element itself
            child_comments = element.xpath('comment()')
            is_deprecated = False
            attrs_list = []
            
            for comment in child_comments:
                if comment.text:
                    comment_text = comment.text.strip()
                    if comment_text.startswith('ch-usage:'):
                        usage = comment_text.replace('ch-usage:', '').strip()
                    elif comment_text.startswith('ch-note:'):
                        note = comment_text.replace('ch-note:', '').strip()
                    elif comment_text.startswith('ch-notice:'):
                        notice = comment_text.replace('ch-notice:', '').strip()
                    elif comment_text == 'ch-referenced':
                        is_referenced = True
                    elif comment_text.startswith('ch-referenced:'):
                        is_referenced = True
                        referenced_name = comment_text.replace('ch-referenced:', '').strip()
                    elif comment_text == 'ch-deprecated':
                        is_deprecated = True
                    elif comment_text.startswith('ch-attrs:'):
                        # Extract attribute list
                        attrs_str = comment_text.replace('ch-attrs:', '').strip()
                        attrs_list = [attr.strip() for attr in attrs_str.split()]
            
            # Get XSD type info
            xsd_info = xsd_type_info.get(elem_name, {})
            card = '1..1'
            xsd_type = 'unknown'
            
            if xsd_info:
                min_occurs = xsd_info.get('min_occurs', '1')
                max_occurs = xsd_info.get('max_occurs', '1')
                card = get_cardinality(min_occurs, max_occurs)
                xsd_type = xsd_info.get('type', 'unknown')
            
            # Determine sub level markers
            sub_markers = ''
            if level > 0:
                sub_markers = '>' * level
                if is_referenced:
                    sub_markers = '<' + sub_markers
            
            # Combine note and notice
            description = note or notice
            
            # Add deprecated notice if needed
            if is_deprecated:
                if description:
                    description += ' NOTE: DEPRECATED'
                else:
                    description = 'NOTE: DEPRECATED'
            
            elements_data.append({
                'sub': sub_markers,
                'element': elem_name,
                'usage': usage,
                'card': card,
                'type': xsd_type,
                'description': description,
                'is_referenced': is_referenced,
                'referenced_name': referenced_name or elem_name,
                'level': level,
                'attributes': attrs_list,
                'is_deprecated': is_deprecated
            })
            
            # Process children ONLY if not referenced
            # When an element is referenced, its children are in a separate template file
            if not is_referenced:
                for child in element:
                    # Only process actual elements, skip comments and text nodes
                    if isinstance(child, etree._Element) and not isinstance(child, etree._Comment):
                        process_element(child, level + 1)
        
        # Start processing from the common ancestor
        for element in common_ancestor.iter():
            # Skip comments and process only elements
            if hasattr(element, 'tag') and not isinstance(element, etree._Comment):
                if element == start_comment.getparent():
                    process_element(element)
                    break
        
        return elements_data
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def generate_markdown_table(data, filename):
    """Generate markdown table from parsed data"""
    if not data:
        return ''
    
    # Sort by level, then by element name
    sorted_data = sorted(data, key=lambda x: (x['level'], x['element']))
    
    markdown = f"# {filename}\n\n"
    markdown += "| Sub | Element | Usage | Card | Type | Description | Note |\n"
    markdown += "|-----|---------|-------|------|------|-------------|------|\n"
    
    for item in sorted_data:
        sub = item['sub']
        element = item['element']
        usage = item['usage']
        card = item['card']
        xsd_type = item['type']
        description = item['description']
        note = item['description']  # Note and description are the same in this context
        
        # Create link if referenced
        if item['is_referenced']:
            link_name = item['referenced_name']
            element = f"[{element}]({link_name}.md)"
        
        markdown += f"| {sub} | {element} | {usage} | {card} | {xsd_type} | {description} | {note} |\n"
        
        # Add attributes if present
        if item['attributes']:
            for attr in item['attributes']:
                attr_usage = 'mandatory'  # Attributes from ch-attrs are always mandatory
                attr_card = '1..1'
                attr_type = 'xsd:string'  # Default type, could be enhanced with XSD lookup
                attr_desc = f"Attribute {attr}"
                
                markdown += f"| {sub} | @{attr} | {attr_usage} | {attr_card} | {attr_type} | {attr_desc} | |\n"
    
    return markdown


def main():
    args = parse_args()
    
    # Load XSD type information
    print(f"Loading XSD from {args.xsd}")
    xsd_type_info = load_xsd_type_info(args.xsd)
    print(f"Loaded {len(xsd_type_info)} type definitions")
    
    # Create output directory
    os.makedirs(args.output, exist_ok=True)
    
    # Process all XML files in input directory
    xml_files = [f for f in os.listdir(args.input) if f.endswith('.xml')]
    
    for xml_file in xml_files:
        print(f"Processing {xml_file}")
        file_path = os.path.join(args.input, xml_file)
        
        # Parse template
        data = parse_template_file(file_path, xsd_type_info)
        
        if data:
            # Generate markdown filename (remove .xml, add .md)
            md_filename = os.path.splitext(xml_file)[0] + '.md'
            md_path = os.path.join(args.output, md_filename)
            
            # Generate markdown content
            element_name = os.path.splitext(xml_file)[0]
            markdown_content = generate_markdown_table(data, element_name)
            
            # Write to file
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"Generated {md_path}")
        else:
            print(f"No data extracted from {xml_file}")
    
    print(f"Processed {len(xml_files)} files")


if __name__ == '__main__':
    main()
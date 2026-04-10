#!/usr/bin/env python3
"""
Script to update XML templates to use <!-- ch-root --> instead of <!-- ch-start --> and <!-- ch-stop -->
"""

import os
import re
import glob

def update_template_file(file_path):
    """Update a single template file"""
    print(f"Processing {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find ch-start and ch-stop patterns
    ch_start_pattern = r'(\s*)<!-- ch-start -->\s*\n(\s*)(<[^>]+>)'
    ch_stop_pattern = r'(\s*)(</[^>]+>)\s*\n(\s*)<!-- ch-stop -->'
    
    # Replace ch-start with ch-root inside the element
    def replace_ch_start(match):
        indent1 = match.group(1)
        indent2 = match.group(2)
        element = match.group(3)
        # Insert ch-root comment before the closing >
        if element.endswith('/>'):
            return f'{indent1}{indent2}{element[:-2]} <!-- ch-root --> />'
        else:
            return f'{indent1}{indent2}{element[:-1]}><!-- ch-root -->'
    
    # Remove ch-stop
    def replace_ch_stop(match):
        indent1 = match.group(1)
        closing_tag = match.group(2)
        return f'{indent1}{closing_tag}'
    
    # Apply replacements
    new_content = re.sub(ch_start_pattern, replace_ch_start, content)
    new_content = re.sub(ch_stop_pattern, replace_ch_stop, new_content)
    
    # Only write if changes were made
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  [OK] Updated {file_path}")
        return True
    else:
        print(f"  - No changes needed for {file_path}")
        return False

def main():
    # Get all XML files in templates directory (excluding ch-profile files)
    xml_files = glob.glob('templates/*.xml')
    
    updated_count = 0
    for xml_file in xml_files:
        # Skip ch-profile files as they're already updated
        if 'ch-profile' in xml_file:
            print(f"Skipping {xml_file} (already updated)")
            continue
            
        if update_template_file(xml_file):
            updated_count += 1
    
    print(f"\nUpdated {updated_count} files")

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""Quick section inserter - adds HTML sections to ders-2.html"""

def insert_section(html_file, section_file, insert_after_line):
    """Insert section content after specified line"""
    with open(html_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    with open(section_file, 'r', encoding='utf-8') as f:
        section = f.readlines()
    
    # Insert section
    new_lines = lines[:insert_after_line] + section + lines[insert_after_line:]
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"✅ Section inserted at line {insert_after_line}")
    print(f"📊 New file length: {len(new_lines)} lines")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python insert_section.py <html_file> <section_file> <line_number>")
        sys.exit(1)
    
    insert_section(sys.argv[1], sys.argv[2], int(sys.argv[3]))

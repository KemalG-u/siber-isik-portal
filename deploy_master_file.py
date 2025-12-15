# Insert Master File into ders-2.html

# Read master file
with open('MASTER_FILE_4_SECTIONS.html', 'r', encoding='utf-8') as f:
    master_sections = f.read()

# Read current ders-2.html
with open('lessons/ders-2.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Insert before </body>
if '</body>' in html_content:
    html_content = html_content.replace('</body>', f'\n\n{master_sections}\n\n</body>')
    print("✅ Inserted before </body>")
elif '</html>' in html_content:
    html_content = html_content.replace('</html>', f'\n\n{master_sections}\n\n</body>\n</html>')
    print("✅ Added </body> and inserted sections")
else:
    html_content += f'\n\n{master_sections}\n</body>\n</html>'
    print("✅ Appended sections with closing tags")

# Write back with UTF-8
with open('lessons/ders-2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ BÜYÜK DÖRTLÜ SENTEZ COMPLETE!")
print(f"✅ Inserted {len(master_sections)} characters")
print(f"✅ Total file: {len(html_content)} characters")

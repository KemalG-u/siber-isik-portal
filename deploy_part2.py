# Deploy Part 2 to ders-2.html and ders-2.css

# Read Part 2 content
with open('PART2_GENERATED.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract HTML sections
html_start = content.find('```html')
html_end = content.find('```', html_start + 7)
html_sections = content[html_start + 7:html_end].strip()

# Extract CSS
css_start = content.find('```css')
css_end = content.find('```',  css_start + 6)
css_code = content[css_start + 6:css_end].strip()

# Extract JavaScript
js_start = content.find('```javascript')
js_end = content.find('```', js_start + 13)
js_code = content[js_start + 13:js_end].strip()

# 1. Add HTML sections to ders-2.html (before </body>)
with open('lessons/ders-2.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

if '</body>' in html_content:
    # Add HTML sections + JavaScript before </body>
    insert_content = f'\n\n{html_sections}\n\n<script>\n{js_code}\n</script>\n\n'
    html_content = html_content.replace('</body>', f'{insert_content}</body>')

with open('lessons/ders-2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ HTML + JavaScript added to ders-2.html")

# 2. Add CSS to ders-2.css
with open('lessons/ders-2.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content += f'\n\n/* PART 2: SECOND WAVE CSS */\n{css_code}\n'

with open('lessons/ders-2.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ CSS added to ders-2.css")
print(f"✅ PART 2 ENTEGRE COMPLETE!")
print(f"   - HTML: {len(html_sections)} chars")
print(f"   - CSS: {len(css_code)} chars")
print(f"   - JS: {len(js_code)} chars")

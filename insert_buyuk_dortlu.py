# BÜYÜK DÖRTLÜ SENTEZ - PYTHON SCRIPT

import re

# Read GOREV2_HTML.txt containing the 3 sections
with open('GOREV2_HTML.txt', 'r', encoding='utf-8') as f:
    gorev2_content = f.read()

# Extract HTML sections between ```html and ```
sections_html = []
parts = gorev2_content.split('```html')
for part in parts[1:]:
    if '```' in part:
        html = part.split('```')[0]
        sections_html.append(html.strip())

# Combine all sections
all_sections = '\n\n'.join(sections_html)

# Read current ders-2.html
with open('lessons/ders-2.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find </body> tag and insert before it
if '</body>' in html_content:
    html_content = html_content.replace('</body>', f'\n{all_sections}\n\n</body>')
else:
    # If no </body>, append to end
    html_content += f'\n{all_sections}\n</body>\n</html>'

# Write back with UTF-8
with open('lessons/ders-2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ BÜYÜK DÖRTLÜ eklendi!")
print(f"✅ {len(sections_html)} section inserted")
print(f"✅ Total HTML: {len(all_sections)} characters")

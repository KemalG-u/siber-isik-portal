import re

# Read GOREV2_HTML.txt and extract HTML sections
with open('GOREV2_HTML.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract HTML sections between ```html and ```
sections = []
parts = content.split('```html')
for part in parts[1:]:  # Skip first part (before first ```html)
    if '```' in part:
        html = part.split('```')[0]
        sections.append(html)

# Combine all 3 sections
all_html = '\n'.join(sections)

# Read ders-2.html
with open('lessons/ders-2.html', 'r', encoding='utf-8') as f:
    main_content = f.read()

# Insert before </body>
updated_content = main_content.replace('</body>', f'\n{all_html}\n</body>')

# Write back
with open('lessons/ders-2.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("✅ 3 sections inserted successfully!")
print(f"Total HTML added: {len(all_html)} characters")

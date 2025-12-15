# Deploy Part 3 Final

# Read Part 3 HTML
with open('PART3_FINAL_HTML.html', 'r', encoding='utf-8') as f:
    html_final = f.read()

# Read Part 3 CSS
with open('PART3_FINAL_CSS.css', 'r', encoding='utf-8') as f:
    css_final = f.read()

# Add HTML before </body>
with open('lessons/ders-2.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

if '</body>' in html_content:
    html_content = html_content.replace('</body>', f'\n{html_final}\n</body>')

with open('lessons/ders-2.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# Add CSS at end
with open('lessons/ders-2.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content += f'\n\n/* PART 3 FINAL */\n{css_final}\n'

with open('lessons/ders-2.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ DERS 2 %100 TAMAMLANDI!")

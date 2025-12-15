# Add @charset to CSS file
with open('lessons/ders-2.css', 'r', encoding='utf-8') as f:
    content = f.read()

if '@charset' not in content:
    content = '@charset "UTF-8";\n\n' + content
    with open('lessons/ders-2.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ @charset added to ders-2.css")
else:
    print("ℹ️ @charset already exists in ders-2.css")

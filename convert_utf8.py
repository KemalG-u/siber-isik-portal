import codecs

# Read UTF-16LE file
with codecs.open('lessons/ders-2.html', 'r', encoding='utf-16-le') as f:
    content = f.read()

# Write as UTF-8
with codecs.open('lessons/ders-2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ ders-2.html converted to UTF-8")

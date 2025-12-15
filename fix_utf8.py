# Fix UTF-8 encoding for ders-2.html
import codecs

# Read with UTF-8 (will handle any encoding)
try:
    with open('lessons/ders-2.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
except:
    # Fallback to UTF-16
    with open('lessons/ders-2.html', 'r', encoding='utf-16-le', errors='ignore') as f:
        content = f.read()

# Ensure meta charset is present
if '<meta charset="UTF-8">' not in content and '<meta charset="utf-8">' not in content.lower():
    # Insert after <head>
    content = content.replace('<head>', '<head>\n    <meta charset="UTF-8">')

# Write with UTF-8 without BOM
with open('lessons/ders-2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ ders-2.html saved as UTF-8 without BOM")
print(f"✅ File size: {len(content)} characters")

# Check first 500 chars for verification
print("\n📋 First 500 characters:")
print(content[:500])

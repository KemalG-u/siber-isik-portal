# 🚑 EMERGENCY: NULL BYTE CLEANUP & ENCODING FIX

import codecs
import os

print("🚨 CODE RED: Starting emergency cleanup...")

# Backup first!
os.system('copy lessons\\ders-2.html lessons\\ders-2.html.BACKUP')
print("✅ Backup created: ders-2.html.BACKUP")

# Read file with UTF-16 (likely source of NULL bytes)
try:
    with codecs.open('lessons/ders-2.html', 'r', encoding='utf-16-le', errors='ignore') as f:
        content = f.read()
    print("✅ Read as UTF-16LE")
except:
    # Try UTF-8 with errors
    with codecs.open('lessons/ders-2.html', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    print("✅ Read as UTF-8 (with error ignore)")

# Remove NULL bytes
original_length = len(content)
content = content.replace('\x00', '')  # Remove NULL bytes
content = content.replace('\u0000', '')  # Unicode NULL
null_removed = original_length - len(content)

print(f"✅ Removed {null_removed} NULL bytes")

# Write clean UTF-8 without BOM
with codecs.open('lessons/ders-2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ File written as UTF-8 without BOM")

# Verify Turkish characters
test_chars = ['ş', 'ğ', 'ü', 'ö', 'ç', 'İ']
found_turkish = any(char in content for char in test_chars)

if found_turkish:
    print("✅ Turkish characters DETECTED")
else:
    print("⚠️  Turkish characters NOT found - may need restoration")

# Check file size
final_size = len(content)
print(f"✅ Final file size: {final_size} characters")

# Verify critical sections
checks = {
    'DOCTYPE': '<!DOCTYPE html>' in content,
    'UTF-8 meta': 'charset="UTF-8"' in content,
    'Yasin Kapısı': 'yasin-kapisi' in content or 'Yasin' in content,
    'Footer': 'site-footer' in content,
}

print("\n📋 VERIFICATION:")
for name, result in checks.items():
    status = "✅" if result else "❌"
    print(f"  {status} {name}")

all_good = all(checks.values())

if all_good and found_turkish:
    print("\n🎉 ENCODING DÜZELDİ. HASTA HAYATTA!")
else:
    print("\n⚠️  Partial recovery - manual check required")

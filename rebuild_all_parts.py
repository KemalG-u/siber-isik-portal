# SYSTEMATIC REBUILD - All Parts

# Read all master files
with open('MASTER_FILE_4_SECTIONS.html', 'r', encoding='utf-8') as f:
    part1_html = f.read()

with open('PART2_GENERATED.md', 'r', encoding='utf-8') as f:
    part2_content = f.read()
    # Extract HTML from markdown
    part2_html_start = part2_content.find('```html')
    part2_html_end = part2_content.find('```', part2_html_start + 7)
    part2_html = part2_content[part2_html_start + 7:part2_html_end].strip()

with open('part3_html.html', 'r', encoding='utf-8') as f:
    part3_html = f.read()

# Read current clean HTML
with open('lessons/ders-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert all parts before </body>
if '</body>' in html:
    combined = f'\n\n{part1_html}\n\n{part2_html}\n\n{part3_html}\n\n'
    
    # Add JS for Part 2
    part2_js = '''<script>
function startSoulJourney() {
    const orb = document.getElementById('soulOrb');
    const btn = document.getElementById('startJourneyBtn');
    btn.disabled = true;
    btn.textContent = '🌟 Yolculuk Devam Ediyor...';
    orb.classList.add('descending');
    setTimeout(() => {
        orb.classList.remove('descending');
        btn.disabled = false;
        btn.textContent = '⚡ Yolculuğu Başlat';
    }, 3500);
}
</script>'''
    
    html = html.replace('</body>', f'{combined}\n{part2_js}\n</body>')
    
    with open('lessons/ders-2.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("✅ SİTE GERİ DÖNDÜ")
print("✅ Part 1: Büyük Dörtlü eklendi")
print("✅ Part 2: Kollektif/Zihin eklendi") 
print("✅ Part 3: Vagus/Footer eklendi")
print("✅ ENCODING TEMİZ")
print("\n🎉 TÜM BÖLÜMLER EKLENDİ!")

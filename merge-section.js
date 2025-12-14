const fs = require('fs');
const path = require('path');

console.log('🔧 Section Merger - Starting...');

// Read main HTML file
const htmlPath = path.join('lessons', 'ders-2.html');
let html = fs.readFileSync(htmlPath, 'utf8');
console.log(`✅ Read ${htmlPath}: ${html.split('\n').length} lines`);

// Read section file
const sectionPath = 'SECTION_4BEDEN.html';
const section = fs.readFileSync(sectionPath, 'utf8');
console.log(`✅ Read ${sectionPath}: ${section.split('\n').length} lines`);

// Find insertion point - before closing script tag
const insertionPoint = '        </script>';
const parts = html.split(insertionPoint);

if (parts.length !== 2) {
    console.error('❌ Could not find insertion point!');
    process.exit(1);
}

// Insert section before closing script
const newHtml = parts[0] + '\n\n' + section + '\n\n' + insertionPoint + parts[1];

// Write back
fs.writeFileSync(htmlPath, newHtml, 'utf8');
console.log(`✅ Written ${htmlPath}: ${newHtml.split('\n').length} lines`);
console.log('🎉 Section merged successfully!');

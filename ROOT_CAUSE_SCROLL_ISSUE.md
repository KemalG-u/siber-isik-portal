# 🚨 ROOT CAUSE BULUNDU!

**Sorun:** Sayfa mobile'da scroll olmuyor!

**Root Cause:** `.genel-niyet-overlay`

```css
.genel-niyet-overlay {
    position: fixed;  /* ← TÜMEN EKRANI KAPLIYOR */
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 9999;    /* ← EN ÜSTTE */
}
```

**Overlay açıkken:**
- Tüm ekranı kaplar
- Scroll oluyor ama overlay altındaki sayfa scroll edilemiyor
- Navigation linklere erişilemiyor!

**Overlay kapalıyken:**
```css
.genel-niyet-overlay.hidden {
    opacity: 0;
    pointer-events: none;  /* ← İYİ AMA YETERSİZ */
}
```

**ÇÖZÜM:**
1. `display: none` ekle `.hidden` class'ına
2. JS auto-close ekle mobilde
3. Test ve push

**ŞİMDİ DÜZELTİYORUM!**

# YASIN KAPISI SECTION - PLACEHOLDER

```html
<!-- YASİN KAPISI SECTION -->
<section id="yasin-kapisi" class="yasin-section">
    <div class="container">
        <h2 class="section-title">
            <span class="section-icon">🌀</span>
            Yasin Kapısı: 3B'den 5B'ye Geçiş
        </h2>
        
        <div class="yasin-placeholder">
            <div class="portal-vortex">
                <div class="vortex-ring ring-1"></div>
                <div class="vortex-ring ring-2"></div>
                <div class="vortex-ring ring-3"></div>
                <div class="portal-center">⚡</div>
            </div>
            
            <div class="loading-text">
                <h3>YASİN KAPISI YÜKLENİYOR...</h3>
                <p>İçerik hazırlanıyor - Claude tarafından sağlanacak</p>
            </div>
        </div>
    </div>
</section>
```

**CSS (ders-2.css'e eklenecek):**

```css
/* YASİN KAPISI SECTION */
.yasin-section {
    background: linear-gradient(135deg, #1a0033 0%, #2d1b4e 100%);
    padding: 80px 20px;
    position: relative;
    overflow: hidden;
}

.yasin-section::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255, 215, 0, 0.05) 0%, transparent 70%);
    animation: pulse 4s ease-in-out infinite;
}

.portal-vortex {
    width: 300px;
    height: 300px;
    margin: 40px auto;
    position: relative;
}

.vortex-ring {
    position: absolute;
    border: 2px solid rgba(255, 215, 0, 0.3);
    border-radius: 50%;
    animation: spin 3s linear infinite;
}

.ring-1 {
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
}

.ring-2 {
    width: 70%;
    height: 70%;
    top: 15%;
    left: 15%;
    animation-duration: 4s;
}

.ring-3 {
    width: 40%;
    height: 40%;
    top: 30%;
    left: 30%;
    animation-duration: 2s;
}

.portal-center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 3rem;
    animation: glow 2s ease-in-out infinite;
}

.loading-text {
    text-align: center;
    color: #FFD700;
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes pulse {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 0.6; }
}

@keyframes glow {
    0%, 100% { filter: drop-shadow(0 0 10px #FFD700); }
    50% { filter: drop-shadow(0 0 30px #FFD700); }
}

@media (max-width: 768px) {
    .portal-vortex {
        width: 200px;
        height: 200px;
    }
}
```

**STATUS:** İskelet hazır, Claude içerik ekleyecek!

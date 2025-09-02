document.addEventListener('DOMContentLoaded', function() {
    const urunleriYukle = async () => {
        try {
            const response = await fetch('fiyatlar.json');
            const urunler = await response.json();
            
            urunleriGoster(urunler);
        } catch (error) {
            console.error('Ürünler yüklenirken hata:', error);
            hataGoster();
        }
    };

    function urunleriGoster(urunler) {
        const container = document.getElementById('urunler');
        const loading = document.querySelector('.loading');
        
        loading.style.display = 'none';
        
        if (urunler.length === 0) {
            container.innerHTML = '<div class="hata">❌ Henüz ürün bulunamadı</div>';
            return;
        }
        
        urunler.forEach(urun => {
            const urunHTML = `
                <div class="urun">
                    <h3>${urun.isim}</h3>
                    <div class="fiyat">${urun.fiyat}</div>
                    <div class="magaza">${urun.magaza}</div>
                    <div class="tarih">${urun.tarih}</div>
                    <a href="${urun.link}" target="_blank" class="incele-btn">🛒 İncele</a>
                </div>
            `;
            container.innerHTML += urunHTML;
        });
    }

    function hataGoster() {
        const container = document.getElementById('urunler');
        const loading = document.querySelector('.loading');
        
        loading.style.display = 'none';
        container.innerHTML = `
            <div class="hata">
                <h3>❌ Ürünler yüklenirken hata oluştu</h3>
                <p>Lütfen daha sonra tekrar deneyin</p>
            </div>
        `;
    }

    // Sayfa yüklendiğinde ürünleri çek
    urunleriYukle();
});

document.addEventListener('DOMContentLoaded', function() {
    const urunleriYukle = async () => {
        try {
            console.log('🔄 Ürünler yükleniyor...');
            
            const response = await fetch('fiyatlar.json');
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const urunler = await response.json();
            console.log('✅ Ürünler alındı:', urunler);
            
            if (!urunler || urunler.length === 0) {
                throw new Error('Ürün listesi boş');
            }
            
            urunleriGoster(urunler);
            
        } catch (error) {
            console.error('❌ Hata:', error);
            hataGoster(error.message);
        }
    };

    function urunleriGoster(urunler) {
        const container = document.getElementById('urunler');
        const loading = document.querySelector('.loading');
        
        loading.style.display = 'none';
        
        container.innerHTML = ''; // Temizle
        
        urunler.forEach(urun => {
            const urunHTML = `
                <div class="urun">
                    <h3>${urun.isim || 'İsimsiz ürün'}</h3>
                    <div class="fiyat">${urun.fiyat || 'Fiyat bilgisi yok'}</div>
                    <div class="magaza">🏪 ${urun.magaza || 'Mağaza bilgisi yok'}</div>
                    <div class="tarih">📅 ${urun.tarih || 'Tarih bilgisi yok'}</div>
                    <a href="${urun.link || '#'}" target="_blank" class="incele-btn">🛒 İncele</a>
                </div>
            `;
            container.innerHTML += urunHTML;
        });
    }

    function hataGoster(mesaj) {
        const container = document.getElementById('urunler');
        const loading = document.querySelector('.loading');
        
        loading.style.display = 'none';
        container.innerHTML = `
            <div class="hata">
                <h3>❌ Ürünler yüklenirken hata oluştu</h3>
                <p>${mesaj}</p>
                <p>Lütfen daha sonra tekrar deneyin veya sayfayı yenileyin</p>
                <button onclick="window.location.reload()">🔄 Sayfayı Yenile</button>
            </div>
        `;
    }

    // 2 saniye bekle ve yükle
    setTimeout(urunleriYukle, 2000);
});

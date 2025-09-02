document.addEventListener('DOMContentLoaded', function() {
    console.log('🔍 Script yüklendi, ürünler yükleniyor...');
    
    const urunleriYukle = async () => {
        try {
            console.log('📦 fiyatlar.json dosyası isteniyor...');
            
            const response = await fetch('fiyatlar.json');
            console.log('📡 Response alındı:', response.status);
            
            if (!response.ok) {
                throw new Error(`HTTP hatası! status: ${response.status}`);
            }
            
            const urunler = await response.json();
            console.log('✅ JSON parse edildi:', urunler);
            
            if (!urunler || urunler.length === 0) {
                throw new Error('Ürün listesi boş veya tanımsız');
            }
            
            console.log(`🎯 ${urunler.length} ürün bulundu`);
            urunleriGoster(urunler);
            
        } catch (error) {
            console.error('❌ Hata:', error);
            hataGoster(error.message);
        }
    };

    function urunleriGoster(urunler) {
        console.log('🖼️ Ürünler gösteriliyor...');
        
        const container = document.getElementById('urunler');
        const loading = document.querySelector('.loading');
        
        if (!container) {
            console.error('❌ #urunler elementi bulunamadı!');
            return;
        }
        
        loading.style.display = 'none';
        container.innerHTML = '';
        
        urunler.forEach((urun, index) => {
            console.log(`📦 Ürün ${index + 1}:`, urun.isim);
            
            const urunHTML = `
                <div class="urun">
                    <div class="urun-resim">
                        <img src="${urun.resim || 'https://picsum.photos/300/200?random=' + Math.random()}" 
                             alt="${urun.isim}" 
                             onerror="this.src='https://via.placeholder.com/300x200?text=Resim+Yok'">
                    </div>
                    <div class="urun-bilgi">
                        <h3>${urun.isim || 'İsimsiz ürün'}</h3>
                        <div class="fiyat">${urun.fiyat || 'Fiyat bilgisi yok'}</div>
                        <div class="magaza">🏪 ${urun.magaza || 'Mağaza bilgisi yok'}</div>
                        <div class="tarih">📅 ${urun.tarih || 'Tarih bilgisi yok'}</div>
                        <a href="${urun.link || '#'}" target="_blank" class="incele-btn">🛒 İncele</a>
                    </div>
                </div>
            `;
            container.innerHTML += urunHTML;
        });
        
        console.log('✅ Ürünler başarıyla gösterildi');
    }

    function hataGoster(mesaj) {
        console.log('❌ Hata gösteriliyor:', mesaj);
        
        const container = document.getElementById('urunler');
        const loading = document.querySelector('.loading');
        
        if (loading) loading.style.display = 'none';
        if (container) {
            container.innerHTML = `
                <div class="hata">
                    <h3>❌ Ürünler yüklenirken hata oluştu</h3>
                    <p>${mesaj}</p>
                    <p>Lütfen daha sonra tekrar deneyin</p>
                    <button onclick="window.location.reload()">🔄 Sayfayı Yenile</button>
                    <br>
                    <small>Browser konsolunda daha fazla detay var (F12)</small>
                </div>
            `;
        }
    }

    // 3 saniye sonra dene (sayfanın tam yüklenmesi için)
    setTimeout(urunleriYukle, 3000);
});

// Global hata yakalama
window.addEventListener('error', function(e) {
    console.error('Global hata:', e.error);
});

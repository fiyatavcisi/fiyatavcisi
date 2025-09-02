function urunleriGoster(urunler) {
    const container = document.getElementById('urunler');
    const loading = document.querySelector('.loading');
    
    loading.style.display = 'none';
    container.innerHTML = '';
    
    urunler.forEach(urun => {
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
}

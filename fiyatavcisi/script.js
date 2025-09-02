// Basit ürün gösterimi
document.addEventListener('DOMContentLoaded', function() {
    const urunler = [
        {
            isim: "Örnek Ürün 1",
            fiyat: "100 TL",
            magaza: "Trendyol",
            indirim: "%25"
        },
        {
            isim: "Örnek Ürün 2", 
            fiyat: "200 TL",
            magaza: "Hepsiburada",
            indirim: "%15"
        },
        {
            isim: "Örnek Ürün 3",
            fiyat: "150 TL", 
            magaza: "n11",
            indirim: "%30"
        }
    ];

    function urunleriGoster() {
        const container = document.getElementById('urunler');
        const loading = document.querySelector('.loading');
        
        loading.style.display = 'none';
        
        urunler.forEach(urun => {
            const urunHTML = `
                <div class="urun">
                    <h3>${urun.isim}</h3>
                    <div class="fiyat">${urun.fiyat}</div>
                    <div class="indirim">${urun.indirim} indirim</div>
                    <div class="magaza">${urun.magaza}</div>
                </div>
            `;
            container.innerHTML += urunHTML;
        });
    }

    // 2 saniye bekle ve ürünleri göster
    setTimeout(urunleriGoster, 2000);
});

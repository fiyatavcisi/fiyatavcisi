// Basit ürün gösterme
const urunler = [
    {isim: "Örnek Ürün 1", fiyat: "100 TL", magaza: "Trendyol"},
    {isim: "Örnek Ürün 2", fiyat: "200 TL", magaza: "Hepsiburada"}
];

function urunleriGoster() {
    const container = document.getElementById('urunler');
    urunler.forEach(urun => {
        container.innerHTML += `
            <div class="urun">
                <h3>${urun.isim}</h3>
                <p class="fiyat">${urun.fiyat}</p>
                <p>Mağaza: ${urun.magaza}</p>
            </div>
        `;
    });
}

// Sayfa yüklendiğinde çalıştır
document.addEventListener('DOMContentLoaded', urunleriGoster);
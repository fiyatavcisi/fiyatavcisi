// script.js en üstüne ekle:
const ornekUrunler = [
  {
    "isim": "iPhone 13 128GB",
    "fiyat": "45.999 TL",
    "magaza": "Trendyol",
    "link": "https://www.trendyol.com/apple/iphone-13-128-gb-apple-turkiye-garantili-p-67948787",
    "tarih": "05.01.2024 15:30",
    "resim": "https://picsum.photos/300/200?random=1"
  }
];

// urunleriYukle fonksiyonunda:
const urunleriYukle = async () => {
    try {
        console.log('📦 fiyatlar.json deneniyor...');
        const response = await fetch('fiyatlar.json');
        
        if (response.ok) {
            const urunler = await response.json();
            urunleriGoster(urunler);
        } else {
            // Fallback: Örnek ürünleri göster
            console.log('⚠️ JSON bulunamadı, örnek ürünler gösteriliyor');
            urunleriGoster(ornekUrunler);
        }
    } catch (error) {
        console.error('❌ Hata:', error);
        // Fallback: Örnek ürünleri göster
        urunleriGoster(ornekUrunler);
    }
};

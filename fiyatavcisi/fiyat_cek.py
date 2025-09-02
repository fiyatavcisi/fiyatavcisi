import json
from datetime import datetime

# Örnek veri ile başlayalım
def ornek_urunleri_olustur():
    urunler = [
        {
            "isim": "iPhone 13 128GB",
            "fiyat": "45.999 TL",
            "magaza": "Trendyol",
            "link": "https://www.trendyol.com/apple/iphone-13-128-gb-apple-turkiye-garantili-p-67948787",
            "tarih": datetime.now().strftime("%d.%m.%Y %H:%M")
        },
        {
            "isim": "Samsung Galaxy S23",
            "fiyat": "39.999 TL",
            "magaza": "Hepsiburada", 
            "link": "https://www.hepsiburada.com/samsung-galaxy-s23",
            "tarih": datetime.now().strftime("%d.%m.%Y %H:%M")
        },
        {
            "isim": "Xiaomi Redmi Note 12",
            "fiyat": "12.999 TL",
            "magaza": "n11",
            "link": "https://www.n11.com/xiaomi-redmi-note-12",
            "tarih": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
    ]
    return urunler

if __name__ == "__main__":
    print("🔄 Örnek ürünler oluşturuluyor...")
    
    try:
        urunler = ornek_urunleri_olustur()
        
        with open('fiyatlar.json', 'w', encoding='utf-8') as f:
            json.dump(urunler, f, ensure_ascii=False, indent=2)
        
        print(f"✅ {len(urunler)} örnek ürün oluşturuldu!")
        
    except Exception as e:
        print(f"❌ Hata: {e}")
        # Boş bir dosya oluştur
        with open('fiyatlar.json', 'w', encoding='utf-8') as f:
            json.dump([], f)
        print("⚠️ Boş dosya oluşturuldu")

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time
import random

def guvenli_istek(url):
    """Bot tespit edilmeden güvenli istek"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        # Rastgele bekleme (bot tespitini önle)
        time.sleep(random.uniform(1.0, 3.0))
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        return response.text
        
    except Exception as e:
        print(f"❌ İstek hatası: {e}")
        return None

def trendyol_urun_ara(urun_adi):
    """Trendyol'da güvenli ürün arama"""
    try:
        arama_terimi = urun_adi.replace(' ', '+')
        url = f"https://www.trendyol.com/sr?q={arama_terimi}&qt={arama_terimi}&st={arama_terimi}"
        
        html = guvenli_istek(url)
        if not html:
            return []
        
        soup = BeautifulSoup(html, 'html.parser')
        urunler = []
        
        # Farklı selector denemeleri
        selectors = [
            'div.p-card-wrppr',
            'div.product-card',
            'div.card-item'
        ]
        
        for selector in selectors:
            urun_kartlari = soup.select(selector)[:3]
            if urun_kartlari:
                break
        
        for kart in urun_kartlari:
            try:
                isim = kart.select_one('[class*="name"], [class*="title"], h3')
                isim = isim.text.strip() if isim else f"{urun_adi} ürünü"
                
                fiyat = kart.select_one('[class*="price"], [class*="prc"], .price-box')
                fiyat = fiyat.text.strip() if fiyat else "Fiyat yok"
                
                # Temizleme
                fiyat = ''.join(c for c in fiyat if c.isdigit() or c in '.,') + ' TL'
                
                urunler.append({
                    'isim': isim,
                    'fiyat': fiyat,
                    'magaza': 'Trendyol',
                    'link': url,
                    'tarih': datetime.now().strftime("%d.%m.%Y %H:%M"),
                    'resim': 'https://picsum.photos/300/200?random=' + str(random.randint(1, 1000))
                })
            except:
                continue
                
        return urunler
        
    except Exception as e:
        print(f"❌ Trendyol hatası: {e}")
        return []

def hepsiburada_urun_ara(urun_adi):
    """Hepsiburada'da güvenli ürün arama"""
    try:
        arama_terimi = urun_adi.replace(' ', '%20')
        url = f"https://www.hepsiburada.com/ara?q={arama_terimi}"
        
        html = guvenli_istek(url)
        if not html:
            return []
        
        soup = BeautifulSoup(html, 'html.parser')
        urunler = []
        
        # Hepsiburada için selector
        urun_kartlari = soup.select('.productListContent-zAP0Y5msy8OHn5z7T_K_, .moria-ProductCard, .search-item')[:3]
        
        for kart in urun_kartlari:
            try:
                isim = kart.select_one('h3, [data-test-id="product-card-name"], .product-name')
                isim = isim.text.strip() if isim else f"{urun_adi} ürünü"
                
                fiyat = kart.select_one('[data-test-id="price-current-price"], .price, .product-price')
                fiyat = fiyat.text.strip() if fiyat else "Fiyat yok"
                
                urunler.append({
                    'isim': isim,
                    'fiyat': fiyat,
                    'magaza': 'Hepsiburada',
                    'link': url,
                    'tarih': datetime.now().strftime("%d.%m.%Y %H:%M"),
                    'resim': 'https://picsum.photos/300/200?random=' + str(random.randint(1, 1000))
                })
            except:
                continue
                
        return urunler
        
    except Exception as e:
        print(f"❌ Hepsiburada hatası: {e}")
        return []

def ornek_urunleri_olustur():
    """Gerçek veri çekilemezse örnek ürünler"""
    return [
        {
            "isim": "iPhone 13 128GB",
            "fiyat": "45.999 TL",
            "magaza": "Trendyol",
            "link": "https://www.trendyol.com/apple/iphone-13-128-gb-apple-turkiye-garantili-p-67948787",
            "tarih": datetime.now().strftime("%d.%m.%Y %H:%M"),
            "resim": "https://picsum.photos/300/200?random=1"
        },
        {
            "isim": "Samsung Galaxy S23",
            "fiyat": "39.999 TL", 
            "magaza": "Hepsiburada",
            "link": "https://www.hepsiburada.com/samsung-galaxy-s23",
            "tarih": datetime.now().strftime("%d.%m.%Y %H:%M"),
            "resim": "https://picsum.photos/300/200?random=2"
        },
        {
            "isim": "Xiaomi Redmi Note 12",
            "fiyat": "12.999 TL",
            "magaza": "n11",
            "link": "https://www.n11.com/xiaomi-redmi-note-12",
            "tarih": datetime.now().strftime("%d.%m.%Y %H:%M"),
            "resim": "https://picsum.photos/300/200?random=3"
        }
    ]

if __name__ == "__main__":
    print("🔄 Akıllı ürün arama başlıyor...")
    
    tum_urunler = []
    arama_urunleri = ["iphone", "samsung", "xiaomi", "laptop", "televizyon"]
    
    for urun in arama_urunleri:
        print(f"🔍 {urun} aranıyor...")
        
        # Trendyol'dan dene
        trendyol_urunler = trendyol_urun_ara(urun)
        if trendyol_urunler:
            tum_urunler.extend(trendyol_urunler)
            print(f"✅ Trendyol'dan {len(trendyol_urunler)} ürün bulundu")
        else:
            print("⚠️ Trendyol'dan ürün bulunamadı")
        
        # Hepsiburada'dan dene
        hepsi_urunler = hepsiburada_urun_ara(urun)
        if hepsi_urunler:
            tum_urunler.extend(hepsi_urunler)
            print(f"✅ Hepsiburada'dan {len(hepsi_urunler)} ürün bulundu")
        else:
            print("⚠️ Hepsiburada'dan ürün bulunamadı")
        
        time.sleep(2)  # Bot tespitini önle
    
    # Eğer hiç ürün bulunamazsa örnek ürünler kullan
    if not tum_urunler:
        print("⚠️ Hiç ürün bulunamadı, örnek ürünler oluşturuluyor...")
        tum_urunler = ornek_urunleri_olustur()
    
    # JSON'a kaydet
    with open('fiyatlar.json', 'w', encoding='utf-8') as f:
        json.dump(tum_urunler, f, ensure_ascii=False, indent=2)
    
    print(f"🎉 Toplam {len(tum_urunler)} ürün kaydedildi!")

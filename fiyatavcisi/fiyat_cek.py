import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def trendyol_urun_ara(urun_adi):
    """Trendyol'da ürün arama"""
    try:
        # Türkçe karakterleri düzelt
        arama_terimi = urun_adi.replace(' ', '%20')
        url = f"https://www.trendyol.com/sr?q={arama_terimi}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        urunler = []
        
        # Ürün kartlarını bul
        urun_kartlari = soup.find_all('div', {'class': 'p-card-wrppr'})[:5]  # İlk 5 ürün
        
        for kart in urun_kartlari:
            try:
                isim = kart.find('span', {'class': 'prdct-desc-cntnr-name'})
                isim = isim.text.strip() if isim else "İsim bulunamadı"
                
                fiyat = kart.find('div', {'class': 'prc-box-dscntd'})
                fiyat = fiyat.text.strip() if fiyat else "Fiyat bulunamadı"
                
                urun_link = kart.find('a', {'class': 'p-card-chldrn-cntnr'})
                urun_link = 'https://www.trendyol.com' + urun_link['href'] if urun_link else "#"
                
                urunler.append({
                    'isim': isim,
                    'fiyat': fiyat,
                    'magaza': 'Trendyol',
                    'link': urun_link,
                    'tarih': datetime.now().strftime("%d.%m.%Y %H:%M")
                })
            except:
                continue
                
        return urunler
        
    except Exception as e:
        print("Hata:", e)
        return []

def hepsiburada_urun_ara(urun_adi):
    """Hepsiburada'da ürün arama"""
    try:
        arama_terimi = urun_adi.replace(' ', '%20')
        url = f"https://www.hepsiburada.com/ara?q={arama_terimi}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        urunler = []
        urun_kartlari = soup.find_all('li', {'class': 'productListContent-zAP0Y5msy8OHn5z7T_K_'})[:5]
        
        for kart in urun_kartlari:
            try:
                isim = kart.find('h3', {'class': 'productListContent-zAP0Y5msy8OHn5z7T_K_'})
                isim = isim.text.strip() if isim else "İsim bulunamadı"
                
                fiyat = kart.find('div', {'data-test-id': 'price-current-price'})
                fiyat = fiyat.text.strip() if fiyat else "Fiyat bulunamadı"
                
                urunler.append({
                    'isim': isim,
                    'fiyat': fiyat,
                    'magaza': 'Hepsiburada',
                    'link': url,
                    'tarih': datetime.now().strftime("%d.%m.%Y %H:%M")
                })
            except:
                continue
                
        return urunler
        
    except Exception as e:
        print("Hata:", e)
        return []

# Test için
if __name__ == "__main__":
    print("🔄 Ürünler aranıyor...")
    
    # Örnek ürünler
    arama_urunleri = ["iphone", "laptop", "televizyon", "kulaklık"]
    
    tum_urunler = []
    
    for urun in arama_urunleri:
        print(f"🔍 {urun} aranıyor...")
        
        # Trendyol'dan ürünleri al
        trendyol_urunler = trendyol_urun_ara(urun)
        tum_urunler.extend(trendyol_urunler)
        
        # Hepsiburada'dan ürünleri al
        hepsi_urunler = hepsiburada_urun_ara(urun)
        tum_urunler.extend(hepsi_urunler)
        
        # 2 saniye bekle (siteyi boğmamak için)
        import time
        time.sleep(2)
    
    # JSON dosyasına kaydet
    with open('fiyatlar.json', 'w', encoding='utf-8') as f:
        json.dump(tum_urunler, f, ensure_ascii=False, indent=2)
    
    print(f"✅ {len(tum_urunler)} ürün bulundu ve kaydedildi!")

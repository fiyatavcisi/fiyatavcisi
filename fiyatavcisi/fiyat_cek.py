import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def trendyol_fiyat_cek(urun_url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(urun_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        urun_adi = soup.find('h1', {'class': 'pr-new-br'})
        urun_adi = urun_adi.text.strip() if urun_adi else "Ürün adı bulunamadı"
        
        fiyat = soup.find('span', {'class': 'prc-dsc'})
        fiyat = fiyat.text.strip() if fiyat else "Fiyat bulunamadı"
        
        return {
            'urun': urun_adi,
            'fiyat': fiyat,
            'magaza': 'Trendyol',
            'tarih': datetime.now().strftime("%d.%m.%Y %H:%M"),
            'url': urun_url
        }
        
    except Exception as e:
        print("Hata:", e)
        return None

# Test için
if __name__ == "__main__":
    urunler = [
        "https://www.trendyol.com/apple/iphone-13-128-gb-apple-turkiye-garantili-p-67948787"
    ]
    
    sonuclar = []
    for url in urunler:
        sonuc = trendyol_fiyat_cek(url)
        if sonuc:
            sonuclar.append(sonuc)
    
    with open('fiyatlar.json', 'w', encoding='utf-8') as f:
        json.dump(sonuclar, f, ensure_ascii=False, indent=2)
    
    print("Fiyatlar güncellendi!")
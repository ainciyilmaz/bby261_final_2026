import requests
from bs4 import BeautifulSoup
import sys

try:
    import rommenu
except ImportError:
    pass 

def etkinlikleri_listele():
    url = "https://etkinlikler.hacettepe.edu.tr/"
    print(f"\n--- Etkinlikler Listesi ({url}) ---")
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            etkinlikler = soup.find_all("div", class_="haber_card_baslik")
            
            if not etkinlikler:
                print("Listelenecek etkinlik bulunamadı.")
            
            count = 1
            for etkinlik in etkinlikler:
                text = etkinlik.get_text().strip()
                if text:
                    print(f"{count}. {text}")
                    count += 1
        else:
            print("Siteye erişilemedi.")
    except Exception as e:
        print(f"Hata: {e}")

def haberleri_listele():
    url = "https://www.bbyhaber.com/feed/"
    print("\n--- Haberler Listesi (BBY Haber RSS) ---")

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Siteye erişilemedi.")
            return

        soup = BeautifulSoup(response.content, "xml")
        haberler = soup.find_all("item")

        if not haberler:
            print("Listelenecek haber bulunamadı.")
            return

        for i, haber in enumerate(haberler[:10], start=1):
            baslik = haber.find("title").get_text(strip=True)
            link = haber.find("link").get_text(strip=True)
            print(f"{i}. {baslik}")
            print(f"   {link}")

    except Exception as e:
        print(f"Hata: {e}")

def ana_uygulama():
    while True:
        try:
            if 'rommenu' in sys.modules:
                if hasattr(rommenu, 'menu'):
                    rommenu.menu()
                elif hasattr(rommenu, 'mainMenu'):
                    rommenu.mainMenu()
                elif hasattr(rommenu, 'ana_menu'):
                    rommenu.ana_menu()
                else:
                    raise ValueError
            else:
                raise ImportError
        except:
            print("\n" + "="*30)
            print("HACETTEPE BİLGİ SİSTEMİ")
            print("1. Etkinlikleri Listele")
            print("2. Haberleri Listele")
            print("3. Uygulamayı Kapat")
        
            secim = input("Seçiminiz (1-3): ")

            if secim == '1':
                etkinlikleri_listele()
            elif secim == '2':
                haberleri_listele()
            elif secim == '3':
                print("Uygulama kapatılıyor...")
                break
            else:
                print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    ana_uygulama()
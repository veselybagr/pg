import sys
import requests
from bs4 import BeautifulSoup  # Import pro parsování HTML

def download_url_and_get_all_hrefs(url):
    
    hrefs = []

    try:
        # Stažení obsahu stránky
        response = requests.get(url)
        
        # Kontrola úspěšnosti požadavku
        if response.status_code == 200:
            # Parsování obsahu stránky pomocí BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Vyhledání všech tagů <a> a extrakce hodnot atributu href
            for a_tag in soup.find_all("a", href=True):
                hrefs.append(a_tag['href'])
        else:
            print(f"Chyba při stahování stránky: HTTP {response.status_code}")
    
    except requests.RequestException as e:
        print(f"Chyba při požadavku na server: {e}")
    
    except Exception as e:
        print(f"Neočekávaná chyba: {e}")

    return hrefs

if __name__ == "__main__":
    try:
        # Načtení URL z argumentu příkazové řádky
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        
        # Výpis nalezených odkazů
        for odkaz in odkazy:
            print(odkaz)
    except Exception as e:
        print(f"Program skončil chybou: {e}")


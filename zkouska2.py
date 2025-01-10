# Příklad 3: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.

import requests

def convert_to_czk(amount, currency):
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    
    # Stažení kurzovního lístku z ČNB
    response = requests.get(url) # Tento požadavek se pokusí stáhnout obsah webové stránky dané adrese.
    if not response.ok:  # Pokud odpověď není úspěšná (chyba při stahování)
        raise ValueError("Chyba při stahování kurzovního lístku.")

    # Rozdělení textu na jednotlivé řádky
    lines = response.text.split("\n")
    rates = {}  # Vytvoříme list, kam uložíme kurzy měn
    
    # Projdeme každý řádek počínaje třetím (první dva jsou hlavička)
    for line in lines[2:]:
        parts = line.split("|")  # Rozdělíme řádek podle "|"
        if len(parts) < 5:  # Pokud řádek nemá dostatek sloupců, přeskočíme ho pomocí continue
            continue
        _, _, mnozstvi, kod, kurz = parts  # Získáme potřebné hodnoty

        # Převedeme hodnoty na čísla:
        # - `kurz.replace(",", ".")` změní desetinnou čárku na tečku (abychom mohli převést na float)
        # - `float(kurz.replace(",", ".")) / float(mnozstvi)` vypočítá kurz pro jednotku dané měny
        rates[kod] = float(kurz.replace(",", ".")) / float(mnozstvi)

    # Ověříme, zda zadaná měna existuje v načtených datech
    if currency not in rates:
        raise ValueError(f"Měna {currency} nebyla nalezena.")

    # Převod částky na české koruny (CZK)
    czk_amount = amount * rates[currency]
    return round(czk_amount, 2)  # Zaokrouhlení výsledku na 2 desetinná místa


# Pytest testy pro Příklad 3
from unittest.mock import patch, MagicMock
def test_convert_to_czk():
    mock_response = """31.10.2025 #237
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,894
EMU|euro|1|EUR|25,480
USA|dolar|1|USD|23,000
Velká Británie|libra|1|GBP|29,745
"""
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, text=mock_response)

        # Příklad 1: Převod 100 USD na CZK
        result = convert_to_czk(100, "USD")
        print(f"Převod 100 USD na CZK: {result} CZK")  # Výpis výsledku převodu

        # Příklad 2: Převod 50 EUR na CZK
        result = convert_to_czk(50, "EUR")
        print(f"Převod 50 EUR na CZK: {result} CZK")  # Výpis výsledku převodu

        # Příklad 3: Převod 200 AUD na CZK
        result = convert_to_czk(200, "AUD")
        print(f"Převod 200 AUD na CZK: {result} CZK")  # Výpis výsledku převodu

        # Příklad 4: Ošetření chybného kódu měny (např. XYZ)
        try:
            result = convert_to_czk(100, "XYZ")
        except ValueError as e:
            print(f"Chyba: {e}")  # Výpis chybové hlášky, pokud měna není v seznamu

# Spuštění testů
test_convert_to_czk()


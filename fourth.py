def je_tah_mozny(figura, cilova_pozice, obsazene_pozice):
    # Funkce pro kontrolu, zda je pozice na šachovnici
    def je_na_sachovnici(pozice):
        return 1 <= pozice[0] <= 8 and 1 <= pozice[1] <= 8

    # Funkce pro kontrolu, zda je cesta mezi dvěma pozicemi volná
    def je_cesta_volna(aktualni, cilova, obsazene_pozice):
        x1, y1 = aktualni
        x2, y2 = cilova

        # Pohyb ve stejné řadě (horizontálně)
        if x1 == x2:
            range_y = range(min(y1, y2) + 1, max(y1, y2))
            for y in range_y:
                if (x1, y) in obsazene_pozice:
                    return False

        # Pohyb ve stejném sloupci (vertikálně)
        elif y1 == y2:
            range_x = range(min(x1, x2) + 1, max(x1, x2))
            for x in range_x:
                if (x, y1) in obsazene_pozice:
                    return False

        # Pohyb diagonálně
        elif abs(x1 - x2) == abs(y1 - y2):
            step_x = 1 if x2 > x1 else -1
            step_y = 1 if y2 > y1 else -1
            for i in range(1, abs(x1 - x2)):
                if (x1 + i * step_x, y1 + i * step_y) in obsazene_pozice:
                    return False

        return True

    # Kontrola, zda je cílová pozice na šachovnici
    if not je_na_sachovnici(cilova_pozice):
        return False

    # Kontrola, zda je cílová pozice volná
    if cilova_pozice in obsazene_pozice:
        return False

    # Získání aktuální a cílové pozice
    aktualni_pozice = figura["pozice"]
    x1, y1 = aktualni_pozice
    x2, y2 = cilova_pozice

    # Pravidla pro jednotlivé figury
    if figura["typ"] == 'pěšec':
        # Pěšec může jít o jedno pole dopředu, pokud pole není obsazené
        if y1 == y2 and x2 == x1 + 1 and (x2, y2) not in obsazene_pozice:
            return True
        # Na výchozím poli (řada 2) může pěšec jít o 2 pole dopředu
        if x1 == 2 and y1 == y2 and x2 == x1 + 2 and \
                (x1 + 1, y1) not in obsazene_pozice and (x2, y2) not in obsazene_pozice:
            return True
        return False

    elif figura["typ"] == 'jezdec':
        # Jezdec se pohybuje do tvaru "L"
        if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
            return True
        return False

    elif figura["typ"] == 'věž':
        # Věž se pohybuje horizontálně nebo vertikálně, cesta musí být volná
        if x1 == x2 or y1 == y2:
            return je_cesta_volna(aktualni_pozice, cilova_pozice, obsazene_pozice)
        return False

    elif figura["typ"] == 'střelec':
        # Střelec se pohybuje diagonálně, cesta musí být volná
        if abs(x1 - x2) == abs(y1 - y2):
            return je_cesta_volna(aktualni_pozice, cilova_pozice, obsazene_pozice)
        return False

    elif figura["typ"] == 'dáma':
        # Dáma kombinuje pohyb věže a střelce
        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            return je_cesta_volna(aktualni_pozice, cilova_pozice, obsazene_pozice)
        return False

    elif figura["typ"] == 'král':
        # Král se pohybuje o jedno pole ve všech směrech
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            return True
        return False

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    # Testy pro pěšce
    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    # Testy pro dámu
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True

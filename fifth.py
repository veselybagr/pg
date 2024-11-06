import sys

# Funkce pro načtení hlavičky souboru
def read_header(file_name, header_length):
    try:
        with open(file_name, 'rb') as f:
            header = f.read(header_length)
            return header
    except FileNotFoundError:
        print(f"Soubor {file_name} nebyl nalezen.")
        sys.exit(1)
    except IOError:
        print(f"Chyba při čtení souboru {file_name}.")
        sys.exit(1)

# Funkce pro kontrolu JPEG formátu
def is_jpeg(header):
    # JPEG začíná byty FF D8 a končí FF D9
    return header[:2] == b'\xFF\xD8' and header[-2:] == b'\xFF\xD9'

# Funkce pro kontrolu GIF formátu
def is_gif(header):
    # GIF začíná byty GIF89a nebo GIF87a
    return header[:6] in [b'GIF89a', b'GIF87a']

# Funkce pro kontrolu PNG formátu
def is_png(header):
    # PNG začíná byty 89 50 4E 47 0D 0A 1A 0A
    return header[:8] == b'\x89PNG\r\n\x1A\n'

# Hlavní funkce, která spustí program
if __name__ == '__main__':
    # Získání názvu souboru z příkazové řádky
    if len(sys.argv) != 2:
        print("Použití: python fifth.py cesta/k/obrazku.jpg")
        sys.exit(1)

    file_name = sys.argv[1]

    # Předdefinovaná délka hlavičky (např. 50 bytů pro kontrolu formátu)
    header_length = 50

    # Načtení hlavičky souboru
    header = read_header(file_name, header_length)

    # Pro ladění: výpis hlavičky souboru (prvních 50 bytů)
    print(f"Prvních {header_length} bytů souboru {file_name}: {header}")

    # Zjištění formátu obrázku
    if is_jpeg(header):
        print(f"Soubor {file_name} je formátu JPEG.")
    elif is_gif(header):
        print(f"Soubor {file_name} je formátu GIF.")
    elif is_png(header):
        print(f"Soubor {file_name} je formátu PNG.")
    else:
        print(f"Soubor {file_name} není žádného známého typu (JPEG, GIF, PNG).")

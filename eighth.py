def bin_to_dec(binarni_cislo):
    # Pokud je vstup typu str, použijeme funkci int() pro převod binárního čísla na desítkové
    if isinstance(binarni_cislo, str):
        return int(binarni_cislo, 2)  # Převede řetězec binárního čísla na desítkový ekvivalent
    # Pokud je vstup typu int, nejprve ho převedeme na řetězec
    elif isinstance(binarni_cislo, int):
        return int(str(binarni_cislo), 2)  # Převede celé číslo na řetězec a pak na desítkový ekvivalent
    else:
        raise ValueError("Vstup musí být buď řetězec nebo celé číslo")

# Testování funkce
def test_funkce():
    assert bin_to_dec("10011101") == 157  # Opravený výsledek binární číslo "10011101" = desítkové 157
    assert bin_to_dec("0") == 0  # Binární číslo "0" = desítkové 0
    assert bin_to_dec(1) == 1  # Binární číslo 1 = desítkové 1
    assert bin_to_dec("100") == 4  # Binární číslo "100" = desítkové 4
    assert bin_to_dec(101) == 5  # Binární číslo 101 = desítkové 5
    assert bin_to_dec("0101") == 5  # Binární číslo "0101" = desítkové 5
    assert bin_to_dec(1000000) == 64  # Binární číslo 1000000 = desítkové 64
    print("Všechny testy prošly!")
# Zavolání testovací funkce pro ověření správnosti
test_funkce()

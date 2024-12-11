def dec_to_bin(cislo):
    # Funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # Napr. 7 -> "111"
    # Napr. 5 -> "101"
    if isinstance(cislo, str):
        cislo = int(cislo)
    return bin(cislo)[2:]

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

def test_edge_cases():
    assert dec_to_bin(0) == "0"
    assert dec_to_bin(255) == "11111111"
    assert dec_to_bin("255") == "11111111"

if __name__ == "__main__":
    import pytest
    pytest.main()


def test_bin_to_dec():
    assert dec_to_bin("0") == "0", "Test selhal pro vstup '0'"
    assert dec_to_bin(1) == "1", "Test selhal pro vstup 1"
    print("test_bin_to_dec prošel!")

def test_edge_cases():
    assert dec_to_bin(0) == "0", "Test selhal pro vstup 0"
    assert dec_to_bin(255) == "11111111", "Test selhal pro vstup 255"
    print("test_edge_cases prošel!")

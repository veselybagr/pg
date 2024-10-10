# funkce vrati treti prvek ze seznamu
def vrat_treti(seznam):
    if len(seznam) < 3:
        return None
    else: 
        return seznam[2]

# funkce spocita prumer z hodnot v seznamu
def udelej_prumer(seznam):
    return sum(seznam) / len(seznam)

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    prumerna_znamka = sum(slovnik["znamky"]) / len(slovnik["znamky"])
    return (f"Jmeno: {slovnik['jmeno']}, Prijmeni: {slovnik['prijmeni']}, Vek: {slovnik['vek']}, Průměrná známka: {round(prumerna_znamka, 2)}  ")


if __name__ == "__main__":
    print(vrat_treti([9,8,7,6,5]))
    print(udelej_prumer([9,8,7,6,5]))
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(naformatuj_text(student))

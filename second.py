def cislo_text(cislo):
    cislo = int(cislo)

    maly_cisla = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest","sedm", "osm", "devět"]
    vetsi_cisla = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    nejvetsi_cisla = ["","", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if cislo < 10:
        return maly_cisla[cislo]
    elif cislo < 20:
        return vetsi_cisla[cislo-10]
    elif cislo < 100:
        deleni = cislo // 10
        zbytky = cislo % 10
        if zbytky == 0:
            return nejvetsi_cisla[deleni]
        else:
            return nejvetsi_cisla[deleni] + " " + maly_cisla[zbytky]
    elif cislo == 100:
        return "sto"
    else:
        return "číslo je mimo rozsah"
    


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)



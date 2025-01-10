# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `process_strings`, která přijme seznam řetězců. 
# Funkce vrátí nový seznam, který obsahuje pouze řetězce delší než 3 znaky, převedené na velká písmena.
# Pokud seznam obsahuje řetězec "STOP", ukončete zpracování seznamu a vraťte dosud vytvořený seznam.



def process_strings(strings):
    # ZDE NAPIŠTE VÁŠ KÓD:
    
    
    
    vysledek = [] # vytvoříme prázdný seznam, kam budeme ukládat naše výsledky
    for řetěz in strings: # cyklus, ten se bude opakovat, dokud..
        if řetěz == "STOP": # pokud cyklus načte "STOP", čtení se ukončí "break"
            break # Ukončí zpracování seznamu
        if len(řetěz) > 3: # pokud je řetězec delší než 3 znaky..
            vysledek.append(řetěz.upper()) # přidá a převede řetězec na velká písmena 
    return vysledek # vrátí výsledný seznam





# Pytest testy pro Příklad 2

def test_process_strings():    
    result = process_strings(["abc", "abcd", "STOP", "efgh"])
    print(f"Výsledek testu 1: {result}") 
    print(f"Očekávaný výsledek 1: ['ABCD']") 
    print("---------------")

    result = process_strings(["hello", "world", "STOP", "python"])
    print(f"Výsledek testu 2: {result}") 
    print(f"Očekávaný výsledek 2: ['HELLO', 'WORLD']") 
    print("---------------")

    result = process_strings(["hi", "ok", "go"])
    print(f"Výsledek testu 3: {result}")  
    print(f"Očekávaný výsledek 3: []") 
    print("---------------")

    result = process_strings(["code", "test", "debug"])
    print(f"Výsledek testu 4: {result}") 
    print(f"Očekávaný výsledek 4: ['CODE', 'TEST', 'DEBUG']")  
    print("---------------")

# Spuštění testů
test_process_strings()
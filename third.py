def je_prvocislo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def vrat_prvocisla(maximum):
    prvocisla = []
    for num in range(2, maximum + 1):
        if je_prvocislo(num):
            prvocisla.append(num)
    return prvocisla


print(je_prvocislo(1))
print(je_prvocislo(2))
print(je_prvocislo(3))
print(je_prvocislo(100))
print(je_prvocislo(101))

print(vrat_prvocisla(1))
print(vrat_prvocisla(2))
print(vrat_prvocisla(3))
print(vrat_prvocisla(10))


# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.


class Shape():

    def area(self):
        return 0.0

# ZDE DOPLŇTE VLASTNÍ KÓD

import math # importoval jsem knihovnu math

class Shape:
    """Základní třída pro geometrické tvary"""
    def area(self):
        raise NotImplementedError("Metoda area() musí být implementována v potomcích.") 

class Rectangle(Shape): # Rectangle zdědí všechny metody a vlastnosti třídy Shape
    """Třída pro obdélník, dědí od Shape"""
    def __init__(self, width, height): #konstruktor odkazujici na aktualni instanci a definuji mu rozmery
        self.width = width 
        self.height = height 

    def area(self):
        """Výpočet plochy obdélníku"""
        return self.width * self.height # vrátí plochu obdélníku

class Circle(Shape): # třída Circle dědí metody a vlastnosti třídy Shape.
    """Třída pro kruh, dědí od Shape"""
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        """Výpočet plochy kruhu (π * r^2)"""
        return math.pi * (self.radius ** 2) # použil jsem implementovanou knihovnu math a zní použíl pí (pi)


from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
from unittest.mock import patch, MagicMock

def test_shapes():
    # Test pro obdélník
    rect = Rectangle(4, 5)
    area_rect = rect.area()
    print(f"Obdélník: {area_rect}") 
    assert area_rect == 20

    # Test pro kruh
    circle = Circle(3)
    area_circle = round(circle.area(), 1)
    print(f"Kruh: {area_circle}")  
    assert area_circle == 28.3

    # Test pro abstraktní třídu Shape
    try:
        shape = Shape()  
    except TypeError:
        print("Nelze vytvořit instanci abstraktní třídy 'Shape'.")
        pass


# Spuštění testů s výpisy
test_shapes()

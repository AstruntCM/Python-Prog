# OOP

# Téglalap Class

class Tegla:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kerulet(self):
        return (self.a + self.b) * 2
    
    def terulet(self):
        return self.a * self.b

tegla = Tegla(4, 5) # Objektum létrehozás

print(tegla.kerulet())
print(tegla.terulet())

#-------------------------------------------------------------

import math

class Kör:
    def __init__(self, r):
        self.r = r
    
    def terület(self):
        return self.r ** 2 * math.pi
    
    def kerület(self):
        return 2 * self.r * math.pi
    
c1 = Kör(5)
c2 = Kör(10)

print(c1.terület())
print(c2.terület())

#--------------------------------------------------------------

# Öröklődés

class Sikidom:
    def ratio(self):
        return self.kerulet() / self.terulet()
    
class Teglalap (Sikidom):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kerulet(self):
        return (self.a + self.b) * 2

    def terulet(self):
        return self.a * self.b
    
class Circle (Sikidom):
    def __init__(self, r):
        self.r = r
    
    def kerulet(self):
        return 2 * self.r * math.pi

    def terulet(self):
        return self.r ** 2 * math.pi
    
shapes = [Teglalap(2, 3), Circle(5), Teglalap(7, 4)]

for shape in shapes:
    print(shape.ratio())

#---------------------------------------------------------------------------

class Masodfok:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def megold(self):
        a, b, c = self.a, self.b, self.c 

        d = b ** 2 - 4 * a * c

        if d > 0:
            return [(-b + d ** 0.5) / (2 * a),
            (-b - d ** 0.5) / (2 * a)]
        elif d == 0:
            return [-b / (2 * a)]
        else:
            return []

Masodfok(1, 3, 2).megold()

#----------------------------------------------------------------------------

class Dog:
    def __init__(self, name, hungry = False):
        self.name = name
        self.hungry = hungry
    
    def eat(self):
        self.hungry = False
    
dogs = [
    Dog('Borzas', True),
    Dog('Vadász', False),
    Dog('Nokedli', False),
    Dog('Cézár', True),
    Dog('Csibész', True)
]

for dog in dogs:
    if dog.hungry:
        print(dog.name)

#----------------------------------------------------------------------------

class Student:
    def __init__(self, name, neptun):
        self.name = name
        self.neptun = neptun

    def __repr__(self):
        return f"Student('{self.name}', '{self.neptun}')"

s = Student('Teszt Elek', 'TTH123')
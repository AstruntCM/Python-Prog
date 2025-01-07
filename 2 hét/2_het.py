# Tuple (Természetes számmal indexelhető, nem módositható tömb)
# Indexelés O(1), vizsgálat alatt O(n) ahol az n = tuple

t = (10, 20, 30)

len(t)

# Elem kiválasztása tupleben
t[0]

# Tupleben lehet több féle tipus is

t = (1, 2, 3, "alma", "körte")

#-----------------------------------------------------------------------

# Lista (Tuple modósitható változata)
# Indexelés O(1), vizsgálat O(n)

l = [10, 30, 20, "alma"]

len(l)

l[1]

# Listában lévő elem modósitása

l[1] = 5

print(l)

# Lista a listában

l = [10, 20, [30, 40]]

# Elem hozzáadás a lista végére

l = [10, 20, 30]

l.append(50)

# Elem hozzáadása egy adott pozicióra

l = [10, 20, 30]

l.insert(2, 3)

# Extend VS append

l = [10, 20, 30]

x = [45, 55]

l.extend(x) # az extend az l listába közvetlenül helyezi bele az x-nek az értékeit. output: [10, 20, 30, 45, 55]

l.append(x) # az append meg az l listában egy új listát tesz bele output: [10, 20, 30, [45, 55]]

# Pop (Listából való törlés)

l = [10, 20, 30, 52]

l.pop(2)

l.pop() # Ebben az esetben az utolsó elemet törli

# Listák összefűzése

l = [10, 20, 30] + ["alma", "sör"] # output: [10, 20, 30, 'alma', 'sör'] 

#-----------------------------------------------------------------------------------------------------------------------

# Halmaz (matematikai halmaz pc-s megfelelője)
# Nincs indexelés, tartalomvizsgálat O(1)
# halmaz = set

s = {10, 20, 30}

20 in s

# Elem hozzáadása a set-hez
s.add(42)

# Unió
{1, 2, 3, 4} | {3, 4, 5} # Output: {1, 2, 3, 4, 5}

# Metszet
{1, 2, 3, 4} & {3, 4, 5} # Output: {3, 4}

# Kivonás
{1, 2, 3, 4} - {3, 4, 5} # Output: {1, 2}

# Nem modósitható elemből bármit hozzá lehet adni pl: tuple.

# Elem törlése
s = {10, 20, 30}

s.remove(20)

#------------------------------------------------------------------------------------------------------------------------

# Szótár (Kulcs érték pár)
# Kulcs -> bármilyen nem modósitható adatszerkezet
# Indexelés O(1)

d = {
      10: 20,
     'alma': 30
    }

len(d)

# Kulcshoz tartozó érték lekérdezése

print(d['alma'])

d['alma'] = 42


# Új key-value pár hozzáadás
d['banán'] = 444

# Érték törlése
del d ["banán"]

# Tuple is lehet akár egy DICT

t = {'a': 10, ('b', 'c'): 20, ('d', ('e', 'f')): 20}
# Input
x = int(input("Add meg a számot: "))

# Print end
print("Hello", end="")
print("Alma", end="")

# Formázott kiírás

x1 = 1.151
x2 = 3.4444

print(f'A megoldás x1 = {x1:.1f} és x2 = %.1f' % (x2))

#--------------------------------------------------------------------------------

# If

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

disz = b**2 - 4 * a * c

if disz > 0:
    x1 = (-b + disz ** 0.5) / (2 * a)
    x2 = (-b - disz ** 0.5) / (2 * a)
    print(f"Két megoldás van, x1 = {x1} és x2 = {x2}")

elif disz == 0:
    x1 = -b / (2 * a)
    print(f"Egy megoldása van, x1 = {x1}")

else:
    print("Nincs megoldás")

#------------------------------------------------------------------------------------

# While

while int (input('Hány pontot értél el? ')) < 16:
    print('Tanulj még!')

print('Gratula')

#-------------------------------------------------------------------------------------

# For

# for ELEM in SZEKVENCIA:
#   UTASITÁS

range(10, 20, 2) # range = tartomány, 10 = alsó, 20 = felső, 2 = lépésköz

n = int(input('n: '))
for i in range(1, n + 1):
    print(i ** 2)

# Háromszög

n = int(input('n: '))

for i in range(n):
    print('*' * (i + 1))

#-------------------------------------------------------------------------------------------------------------

s = 'venividivici'
offset = 3

t = ''

for ch in s:
    ch2 = chr((ord(ch) - ord('a') + offset) % 26 + ord('a'))
    t += ch2

print(t)

#------------------------------------------------------------------------------------------------------
import random
x = random.randint(1, 100)

y = None
while y != x:
    y = int(input('Tipp: '))

    if y > x:
        print('Nagy')
    elif y < x:
        print("Kicsi")
    else:
        print('Eltaláltad')

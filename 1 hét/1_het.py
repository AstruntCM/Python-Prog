# változó meghatározása
i = 11

# röviditett érték hozzáadás
j = 0

j += 1

# Lebegőpontos osztás
h = 7 / 3

# Egészosztás
h = 7 // 3

# Hatványozás
h = 10 ** 12

# Maradék képzéses osztás
j = 17 % 7

# Komplex Számok (j == komplex számmal (i))
hk = (2 + 3j) / (5 - 3.5j)

# STR char-ra bontás
s = "alma"

t = s[0]

# STR tartalmazza-e?
st = "almakörtebarack"

print("al" in st)

# STR-ből bájtba konvertálás
b = 'Géza'.encode('utf-8')

print(b)

print(len('á'.encode('utf-8')))

# Bájtból STR-be
b = b.decode('utf-8')

print(b)

# White Space eltávolitása

a = '  \talma\n'.strip()

print(a)

a = '---kapa+++'.strip('+-')

print(a)

# Kicsi betűvé alakitás
t = 'Álmos'.lower()

# Nagy betűvé alakitás
h = 'kuka'.upper()

# Logikai tagadás
x = True

not x
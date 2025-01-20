# Feltétel nélküli comprehension

l = []
for i in range(1, 11):
    l.append(i**2)
print(l)

# Comprehension-nel ugyanez

l = [i**2 for i in range(1, 11)]
print(l)

# Set

s = {i**2 for i in range(1, 11)}
print(s)

# Dict
d = {}

for ch in 'aeiou':
    d[ch] = ord(ch)
print(d)

# Dict comprehension

d = {ch: ord(ch) for ch in 'aeiou'}
print(d)

#----------------------------------------------------------------------------

# Feltételes comprehension

[i ** 2 for i in range(1, 11) if i % 2 == 0]

{ch: ord(ch) for ch in 'aeiou' if ch in {'a', 'u'}}

#----------------------------------------------------------------------------

# Rendezés

l = [10, 20, 5]

l.sort()

d = {'b': 10, 'c': 20, 'a': 30}
sorted(d)


#---------------------------------------------------------------------------

# Fájlkezelés

f = open('példa.txt', 'r')
s = f.read()
f.close()

f.readline() # csak egy sort olvas be

s.split(',') # vesszőnél szedi széjjel a szöveget

# For loop

f = open('egy.txt', "r")

for line in f:
    print(line.strip())
f.close()

# tömbök a tömben

data = []

f = open('példa.txt')
f.readline()
for line in f:
    tok = line.strip().split(',')
    data.append([tok[0], float(tok[1])])
f.close()

# Írás

s = 'Géza, kék az ég.'
f = open('example_file_2.txt', 'w')
f.write(s)
f.close()

#------------------------------------------------------------------------------------------
# Hamlet
szavak = open('hamlet.txt').read().lower().split()

import string

szavak = [szo.strip(string.punctuation) for szo in szavak]

frek = {}

for szo in szavak:
    if szo in frek:
        frek[szo] += 1
    else:
        frek[szo] = 1

frek2 = sorted([(x[1], x[0]) for x in frek.items()], reverse=True)

for i in range(30):
    print(f'{frek2[i][1]}: {frek2[i][0]}')
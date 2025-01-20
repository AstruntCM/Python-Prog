# Unpacking

x, (y, z) = 10, [['a', 'b'], 'qqq']

print(x) # x = 10

# For ciklussal

pairs = [('alma', 10), ('körte')]

#--------------------------------------------------

# Slicing

# szintaxis: alsó határ: felső határ: lépésköz

foo = [10, 20, 'kutya', 'macska', [1, 2]]

foo[1: 4: 1] # 1, 2, 3-s indexű elemet választja ki

foo[:2] # első 2 elem

foo[:-1] # összes elem kivétel az utolsó

foo[::2] # páros indexű elemek

foo[1::2] # páratlan indexű elemek

foo[::-1] # hátulról előre

#------------------------------------------------------

# Enumerate

data = ['alma', 'körte', 'szilva']
for i in range(len(data)):
    print(i, data[i])

# Enumerate-tel

data = ['alma', 'körte', 'szilva']

for i, x in enumerate(data):
    print(i, x) # Output: 0 alma, 1 körte, 2 szilva

# Enumerate kicsomagolás nélkül

for y in enumerate(data):
    print(y[0], y[1])

# Listává alakitás

list(enumerate(data))

#----------------------------------------------------------

# Zip

l1 = ['kék', 'zöld', 'fehér']
l2 = [10, 20, 30]
for i in range(len(l1)):
    print(l1[i], l2[i])

# Zippel

l1 = ['kék', 'zöld', 'fehér']
l2 = [10, 20, 30]
for x, y in zip(l1, l2):
    print(x, y) # Output: kék 10, zöld 20, fehér 30

# Több listára használható

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = [10, 20, 30]
list(zip(l1, l2, l3))

# Kicsomagolás nélkül is müködik

for z in zip(l1, l2):
    print(z[0], z[1])

#-----------------------------------------------------------------

s = 'alma,10,körte,20,barack,30,szilva,40'

sp = s.split(',')

d = dict(zip(sp[::2], sp[1::2]))
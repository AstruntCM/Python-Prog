# Függvények

def root(x, n = 2):
    '''Returns the n-th root of x.'''
    return x ** (1 / n)

# Függvény a fv.-ben

def f(y):
    def g(x):
        return x * y
    return g

g2 = f(2)
g3 = f(3)

#--------------------------------------------------------------------

# Prim check

def prim(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

prim(1) # --> False

prim(3) # --> True

#-------------------------------------------------------------------

# Legnagyobb közös osztó

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

#------------------------------------------------------------------

# Lambda Kifejezés

f = lambda x: x + 2

f(10) # --> O: 12

pairs = [('alma', 30), ('körte', 10), ('barack', 20)]
sorted(pairs, key = lambda x: x[1])

freq = {'king': 789, 'queen': 655, 'castle': 11}
sorted(freq, key = lambda x: -freq[x])

#------------------------------------------------------------------

# Premier League

games = []

ft = open('pre.txt')

for i in range(6):
    ft.readline()

for sor in ft:
    tok = sor.split('\t')
    games.append({
        'mérköz': int(tok[0]),
        'hazai': tok[1],
        'vendeg': tok[2],
        'hazaigol': int(tok[3]),
        'vendeggol': int(tok[4])
    })

ft.close()

print(games)
# Függvények

def root(x, n = 2):
    '''Returns the n-th root of x.'''
    return x ** (1 / n)

# Függvény a fv.-ben

def ftt(y):
    def g(x):
        return x * y
    return g

g2 = ftt(2)
g3 = ftt(3)

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

ft = lambda x: x + 2

ft(10) # --> O: 12

pairs = [('alma', 30), ('körte', 10), ('barack', 20)]
sorted(pairs, key = lambda x: x[1])

freq = {'king': 789, 'queen': 655, 'castle': 11}
sorted(freq, key = lambda x: -freq[x])

#------------------------------------------------------------------

# Premier League

games = []
f = open('5 het/pl.txt')
for i in range(6): # első 6 sor átugrása
    f.readline()
for line in f: # további sorok feldolgozása
    tok = line.split('\t')
    games.append({
        'round': int(tok[0]),
        'hteam': tok[1],
        'ateam': tok[2],
        'hgoals': int(tok[3]),
        'agoals': int(tok[4])
    })
f.close()

#------------------------------------------
# 1. feladat
# Mérközés hány % volt gól

gol = 0

for i in games:
    if i['hgoals'] + i['agoals'] > 0:
        gol += 1

szazalek = gol / len(games) * 100

#----------------------------------------

# 2. feladat
# Melyik mérközésen volt a legtöbb gól?

gmax = -1

for i in games:
    gol = i['hgoals'] + i['agoals']
    if gol > gmax:
        gmax = gol
        gbest = i

print(gbest)

#---------------------------------------

n = 2

stats = {}

for g in games:
    if g['round'] <= n:
        hteam = g['hteam']
        ateam = g['ateam']
        hgoals = g['hgoals']
        agoals = g['agoals']
        
        if hteam not in stats:
            stats[hteam] = [0, 0, 0]
        if ateam not in stats:
            stats[ateam] = [0, 0, 0]
        
        if hgoals > agoals: # a hazai csapat nyert
            stats[hteam][0] += 3
        elif hgoals == agoals: # döntetlen
            stats[hteam][0] += 1
            stats[ateam][0] += 1
        else: # a vendégcsapat nyert
            stats[ateam][0] += 3
            
        stats[hteam][1] += hgoals - agoals
        stats[ateam][1] += agoals - hgoals
        stats[hteam][2] += hgoals
        stats[ateam][2] += agoals

print(stats)
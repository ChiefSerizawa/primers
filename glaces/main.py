import sys
import math
import random

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest(p, shops):
    dmin    = sys.maxsize
    closest = None
    for idx in range(0, len(shops)):
        d = dist(p, shops[idx])
        if d < dmin:
            dmin    = d
            closest = idx
    return closest, dmin

def score(shops, density):
    h = len(density)
    w = len(density[0])
    dtot = 0
    tot  = 0
    for i in range(0, h):
        for j in range(0, w):
            shop_idx, dmin = closest((i, j), shops)
            dtot += density[i][j] * dmin
            tot  += density[i][j]
    return dtot/tot

def inbound(p, h, w):
    return p[0] > 0 and p[0] < h and p[1] > 0 and p[1] < w

def move(i, shops, density, moveable, best_score):
    h = len(density)
    w = len(density[0])
    if not moveable:
        return shops[i]

    up         = (shops[i][0] + 1 , shops[i][1]    )
    down       = (shops[i][0] - 1 , shops[i][1]    )
    left       = (shops[i][0]     , shops[i][1] - 1)
    right      = (shops[i][0]     , shops[i][1] + 1)
    up_right   = (shops[i][0] + 1 , shops[i][1] + 1)
    up_left    = (shops[i][0] + 1 , shops[i][1] - 1)
    down_right = (shops[i][0] - 1 , shops[i][1] + 1)
    down_left  = (shops[i][0] - 1 , shops[i][1] - 1)

    arounds = [up, down, left, right, up_right, up_left, down_right, down_left]
    best     = shops[i]
    for around in arounds:
        if inbound(around, h, w):
            shops[i] = around
            scr = score(shops, density)
            if scr < best_score:
                best = around
                best_score = scr

    shops[i] = best
    return best_score

f    = open(sys.argv[1])
line = f.readline()
w, h, n = list(map(int, line.split(',')))

density = []
for line in f:
    density.append(list(map(int, line.split(','))))

shops    = []
moveable = []

for i in range(0, n):
    r = random.randint(0, h)
    c = random.randint(0, w)
    shops.append((r, c))
    moveable.append(True)

upgrade = True
best_score = score(shops, density)
while upgrade:
    for i in range(0, n):
        best_score = move(i, shops, density, moveable, best_score)
        for i in range(0, n):
            print('{0[1]},{0[0]}'.format(shops[i]))
        print(best_score)
        print()

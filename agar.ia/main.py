import sys
import math
import copy
import time

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))

def find_closest(xy, cells, k):
    res = []
    min_dist   = 0
    furthest   = 0
    for id, cell in cells.items():
        d = dist(xy, cell['xy'])
        if len(res) < k:
            res.append((id, d))
        elif (d < res[-1][1]):
            res.pop()
            res.append((id, d))
        res = sorted(res, key=lambda r: r[1])
    return res

def deep_search(xy, cells, k, n, way, best_way):
    closest = find_closest(xy, cells, k)
    if n == 1:
        way['path'].append(closest[0][0])
        way['d'] += closest[0][1]
#        print("Examined:", way)
#        print("Best way:", best_way)
        if way['d'] < best_way['d']:
#            print('NEW BEST')
            best_way = copy.deepcopy(way)
        way['path'].pop()
        way['d'] -= closest[0][1]
        return best_way
    for id_dist in closest:
        next_cell = cells.pop(id_dist[0])
        way['path'].append(next_cell['id'])
        way['d'] += id_dist[1]
        best_way = deep_search(next_cell['xy'], cells, k, n-1, way, best_way)
        cells[id_dist[0]] = next_cell
        way['path'].pop()
        way['d'] -= id_dist[1]
    return best_way

f = open(sys.argv[1])
T = int(f.readline())

line = f.readline()
cells = {}
while line:
    values = list(map(int, line.split(',')))
    id = values[0]
    xy = values[1:]
    cell = {'id': id, 'xy': xy}
    cells[id] = cell
    line = f.readline()

current_xy = [0, 0]
t = T
l = 0

k, n = 4, 5
while t > 0 and len(cells) > 0:
    way = {'path': [], 'd': 0}
    best_way = {'path': [], 'd': sys.maxsize}

    #print('Loop:', l)
    best_way = deep_search(current_xy, cells, k, n, way, best_way)
    #print('Best:', best_way)
    for id in best_way['path']:
        cell = cells.pop(id)
        t -= dist(current_xy, cell['xy'])
        current_xy = cell['xy']
        if t > 0:
            print(cell['id'])
            #print(t)

    #print('Current:', current_xy)
    l += 1

#closest = find_closest(prev, cells, 1)
#print(closest)
#for c in closest:
#    print(cells[c[0]])
#print()
#
#closest = find_closest(prev, cells, 2)
#print(closest)
#for c in closest:
#    print(cells[c[0]])
#print()
#
#closest = find_closest(prev, cells, 3)
#print(closest)
#for c in closest:
#    print(cells[c[0]])
#print()
#
#closest = find_closest(prev, cells, 4)
#print(closest)
#for c in closest:
#    print(cells[c[0]])
#print()
#
#closest = find_closest(prev, cells, 5)
#print(closest)
#for c in closest:
#    print(cells[c[0]])
#
#
#


















#prev_xy   = [i, j]
#t = T
#cells = copy.deepcopy(init)
#
#k = 2
#n = 2
#while t > 0:
#    min_dist    = sys.maxsize
#    index       = 0
#    res         = find_closest(prev_xy, cells, k)
#    for tpl in res:
#        cells.pop(tpl[0])
#        deep_search(cells[tpl[0]]['xy'], n-1)
#    while(n > 0)
#        for tpl in res:
#
#            d = dist(prev_xy, cell['xy'])
#            if d < min_dist:
#                min_dist        = d
#                next_cell_index = index
#            index += 1
#        next_cell = cells.pop(next_cell_index)
#    prev_xy = next_cell['xy']
#    t -= min_dist
#    if t > 0:
#        #print(next_cell['id'])
#        count += 1
#

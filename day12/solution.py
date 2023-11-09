import pdb
import numpy as np
import string
from collections import deque

letters = list(string.ascii_lowercase)
conversion = {v:k+1 for k,v in enumerate(letters)}
maxval = max([v for v in conversion.values()])
conversion.update({'S':0, 'E':maxval+1})

with open('in.txt', 'r') as f:
    entry = f.readlines()

heightmap = list()
for line in entry:
    line = list(line.strip())
    line = [conversion[x] for x in line]
    heightmap.append(line)

hmap = np.array(heightmap)
hmap = hmap.reshape(len(heightmap),len(line))
hmap = np.pad(hmap,1, mode='constant', constant_values=99)
start = (np.where(hmap==0)[0][0], np.where(hmap==0)[1][0])

path = deque()
path.append(start)
#print(hmap)

def next(coord, hmap, prev=None):
    value = hmap[coord]
    out = list()
    up = (coord[0]+1,coord[1])
    down = (coord[0]-1,coord[1])
    left = (coord[0],coord[1]-1)
    right = (coord[0], coord[1]+1)

    if prev != up:
        if (hmap[up] <= value or hmap[up] == value+1):
            out.append(up)
    if prev != down:
        if (hmap[down] <= value or hmap[down] == value+1):
            out.append(down)
    if prev !=left:
        if (hmap[left] <= value or hmap[left] == value + 1):
            out.append(left)
    if prev !=right:
        if hmap[right] <= value or hmap[right] == value+1:
            out.append(right)
    return out

def check_end(coord, hmap):
    if hmap[coord] == 27:
        return True
    else:
        return False

def count_steps(start, hmap):
    P = deque()
    P.append(start)
    steps = 0
    middle = [start]
    flag = True
    while flag:
        for coordinates in middle:
            if check_end(coordinates,hmap):
                flag = False
                break
        if flag is True:
            steps += 1
        t = deque()
        for coordinate in middle:
            next_steps = next(coordinate, hmap)
            next_steps = [x for x in next_steps if x not in P]
            t.extend(next_steps)
            P.extend(next_steps)
        if not t:
            return None
        middle.clear()
        middle = list(set(t))
    return steps

print("Part 1")
print(count_steps(start,hmap))


##### PART 2 #####
print("Part 2")

c = 0
steps_list = list()
rows = hmap.shape[0]
cols = hmap.shape[1]
for r in range(rows):
    for c in range(cols):
        if hmap[r,c] == 1:
            
            start = (r,c)
            #print(start)
            steps = count_steps(start,hmap)
            if steps:
                #print("start: {}, steps: {}".format(start,steps))
                steps_list.append(steps)
print("solution: ")
print(sorted(steps_list)[0])

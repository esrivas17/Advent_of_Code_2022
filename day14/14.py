import pdb
import sys
arg = sys.argv[1]
#print(sys.argv)
print(arg)

with open(arg, 'r') as f:
    entry = f.readlines()

field = set()

def fill_list(c1, c2, s):
    x1, x2 = c1[0], c2[0]
    y1, y2 = c1[1], c2[1]
    if x1 == x2:
        if y1 > y2:
            while y1 >= y2:
                s.add((x1,y2))
                y2 += 1
        else:
            while y2 >= y1:
                s.add((x1,y1)) 
                y1 += 1
    elif y1 == y2:
        if x1 > x2:
            while x1 >= x2:
                s.add((x2,y1))
                x2 += 1
        else:
            while x2 >= x1:
                s.add((x1,y1))
                x1 += 1    

for line in entry:
    coords = line.split("->")
    for c1,c2 in zip(coords,coords[1:]):
        x0,y0 = map(int, c1.strip().split(","))
        x1,y1 = map(int, c2.strip().split(","))
        fill_list((x0,y0), (x1,y1), field)
    

#print(field)

start = (500,0)
max_y = max([x[1] for x in field])

dust = set()

def simulation(start, field, dust, thres):
    x0, y0 = start
    if y0 >= thres:
        return False
    down, d_left, d_right = (x0, y0+1), (x0-1, y0+1), (x0+1, y0+1)
    if down not in field and down not in dust:
        return simulation(down,field, dust, thres)
    elif d_left not in field and d_left not in dust:
        return simulation(d_left,field, dust, thres)
    elif d_right not in field and d_right not in dust:
        return simulation(d_right,field, dust,thres)
    else:
        dust.add(start)
        return True

while True:
    rc = simulation(start, field, dust, max_y)
    if not rc:
        break

print(dust)
print("Answer part1: {}".format(len(dust)))

##### PART 2 ####
floor = max_y+2
max_x = max([x[0] for x in field])
min_x = min([x[0] for x in field])
inf_x0 = (min_x-2000, floor)
inf_x1 = (max_x+2000, floor)

fill_list(inf_x0, inf_x1, field)

def sim_p2(start, field, dust):
    x0, y0 = start
    down, d_left, d_right = (x0, y0+1), (x0-1, y0+1), (x0+1, y0+1)
    if down not in field and down not in dust:
        return sim_p2(down, field, dust)
    elif d_left not in field and d_left not in dust:
        return sim_p2(d_left, field, dust)
    elif d_right not in field and d_right not in dust:
        return sim_p2(d_right,field, dust)
    else:
        if start == (500,0):
            dust.add(start)
            return False
        else:
            dust.add(start)
            return True

while True:
    rc = sim_p2(start, field, dust)
    if not rc:
        break

print("Answer part2: {}".format(len(dust)))    

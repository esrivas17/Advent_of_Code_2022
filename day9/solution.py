with open('p2.ex', 'r') as f:
    entry = f.readlines()

xh = [0]
yh = [0]
direction = ['x']
for line in  entry:
    line = line.strip().split()
    step = int(line[1])
    move = line[0]
    for step in range(0,step):
        direction.append(move)
        if move == 'U':
            yh.append(yh[-1]+1)
            xh.append(xh[-1])
        elif move == 'D':
            yh.append(yh[-1]-1)
            xh.append(xh[-1])
        if move == 'L':
            xh.append(xh[-1]-1)
            yh.append(yh[-1])
        elif move == 'R':
            xh.append(xh[-1]+1)
            yh.append(yh[-1])
            

xt = [0]
yt = [0]
from math import sqrt
def func(xh,yh,xt,yt):
    f1 = (xh-xt)*(xh-xt)
    f2 = (yh-yt)*(yh-yt)
    d = sqrt(f1+f2)
    if d > sqrt(2):
        return False
    else:
        return True

def dist(xh, yh, xt, yt):
    if abs(xh-xt) > 1:
        return False
    elif abs(yh-yt) > 1:
        return False
    else:
        return True

la = list()
tlist = list()
for i, z in enumerate(zip(xh,yh)):
    x, y = z
    if not dist(x,y,xt[-1],yt[-1]):
        if (xh[i-1],yh[i-1]) not in tlist:
            tlist.append((xh[i-1],yh[i-1]))
        xt.append(xh[i-1])
        yt.append(yh[i-1])
    else:
        if (xt[-1],yt[-1]) not in tlist:
            tlist.append((xt[-1],yt[-1]))
        xt.append(xt[-1])
        yt.append(yt[-1])

tail = list()
head = list()
print("head: {}, tail: {}".format(len(xh),len(yt)))
for x,y,a,b in zip(xt,yt, xh, yh):
    if (x,y) not in tail:
        tail.append((x,y))
    head.append((a,b))

print("tail list: {}".format(len(tlist)))
print("set tail: {}".format(len(list(set(tail[:])))))
print("other: {}".format(len(la)))
#print(la)
#guess1 6208 guess2 9223

########## PART 2 ##########
print("PART2")
print(len(xh))
for n in range(0,10):
    tlist = list()
    xt = [0]
    yt = [0]
    for i, z in enumerate(zip(xh,yh)):
        x, y = z
        if not dist(x,y,xt[-1],yt[-1]):
            if (xh[i-1],yh[i-1]) not in tlist:
                tlist.append((xh[i-1],yh[i-1]))
            xt.append(xh[i-1])
            yt.append(yh[i-1])
        else:
            if (xt[-1],yt[-1]) not in tlist:
                tlist.append((xt[-1],yt[-1]))
            xt.append(xt[-1])
            yt.append(yt[-1])
    xh = xt[1:]
    yh = yt[1:]
    print(len(tlist))

print("Part 2")
print(len(tlist))

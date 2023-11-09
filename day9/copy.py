with open('in.txt', 'r') as f:
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

test = list()
tail_dir = list()
for i, z in enumerate(zip(xh,yh,direction)):
    x, y, m = z
#    print(i)
    if not dist(x,y,xt[-1],yt[-1]):
        print(xh[-2])
        if m == 'U':
            if (x,y-1) not in test:
                test.append((x,y-1))
            xt.append(x)
            yt.append(y-1)
        elif m == 'D':
            if (x,y+1) not in test:
                test.append((x,y+1))
            xt.append(x)
            yt.append(y+1)
        elif m == 'L': 
            if (x+1,y) not in test:
                test.append((x+1,y))
            xt.append(x+1)
            yt.append(y)
        elif m == 'R':
            if (x-1,y) not in test:
                test.append((x-1,y))
            xt.append(x-1)
            yt.append(y)
    else:
        if (xt[-1],yt[-1]) not in test:
            test.append((xt[-1],yt[-1]))
        xt.append(xt[-1])
        yt.append(yt[-1])

tail = list()
head = list()
print("head: {}, tail: {}".format(len(xh),len(yt)))
for x,y,a,b in zip(xt,yt, xh, yh):
    tail.append((x,y))
    head.append((a,b))

print("test: {}".format(len(test)))
print(len(list(set(tail[1:]))))


print(xh)
########## PART 2 ##########


import pdb
import numpy as np
import matplotlib.pyplot as plt 

with open('in.txt', 'r') as f:
    entry = f.readlines()

max_x, min_x = list(), list()
max_y, min_y = list(), list()
xx = list()
yy = list()
for line in entry:
    line = line.strip().split("->")
    line = [x.strip() for x in line]
    for ele in line:
        cx = int(ele.split(",")[0])
        cy = int(ele.split(",")[1])
        xx.append(cx)
        yy.append(cy)
    maxx = max([int(x.split(",")[0]) for x in line])
    minx = min([int(x.split(",")[0]) for x in line])
    maxy = max([int(x.split(",")[1]) for x in line])
    miny = min([int(x.split(",")[1]) for x in line])
    max_x.append(maxx)
    min_x.append(minx)
    max_y.append(maxy)
    min_y.append(miny)

x1 = max(max_x)
x0 = min(min_x)
rgx = x1 - x0
y1 = max(max_y)
y0 = min(min_y)
rgy = y1 - y0
print("Min x: {} , Max x: {}".format(x0,x1))
nx1 = max(xx)
nx0 = min(xx)
print("New min x: {}, max x: {}".format(nx0, nx1))

field = np.array(list('.'*(rgx+1)*(y1+1)), dtype=str)
field = field.reshape((y1+1,rgx+1))
#pdb.set_trace()
f2 = np.array(list('.'*(x1+1)*(y1+1)), dtype=str)
f2 = f2.reshape((y1+1,x1+1))

def replace_rock(c1,c2,field, rg):
    x1 = int(c1.split(",")[0])
    y1 = int(c1.split(",")[1])
    x2 = int(c2.split(",")[0])
    y2 = int(c2.split(",")[1])
    if y1 == y2:
        if x1 > x2:
            field[y1,x2-rg:x1+1-rg] = '#'
        elif x1 < x2:
            field[y1,x1-rg:x2+1-rg] = '#'
    elif x1 == x2:
        if y1 > y2:
            field[y2:y1+1,x1-rg] = '#'
        elif x1 < x2:
            field[y1:y2+1,x1-rg] = '#'
    return field


for line in entry:
    line = line.strip().split("->")
    line = [x.strip() for x in line]
    for c1,c2 in zip(line[1:],line[:-1]):
        #field = replace_rock(c1,c2,field,x0)
        f2 = replace_rock(c1,c2,f2,0)
field[0,500-x0] = '+' #start_sand
f2[0,499] = '+'
pdb.set_trace()
#print(field)
################# FILLING WITH SAND ######################

def replace(coord, field):
    if field[coord] != '+' and field[coord] == 'o':
        field[coord] = '.'


def check(coord, field):
    if field[coord] == '.':
        return True
    else:
        return False

def check_block(coord,field):
    if field[coord] == '#':
        return True
    else:
        return False

def boundaries(list_coord, field):
    ydim, xdim = field.shape
    for coord in list_coord:
        y, x = coord
        if y > ydim-1 or y < 0:
            return False
        if x > xdim-1 or x < 0:
            return False
        
    return True


def fall_down(origin, field):
    y0, x0 = origin
    down, diag_left, diag_right = (y0+1,x0), (y0+1, x0-1), (y0+1, x0+1)
    left, right = (y0,x0-1), (y0,x0+1)
    if not boundaries([down, diag_left, diag_right], field):
        replace(origin, field)
        return 'bounds'
    if check(down, field):
        field[down] = 'o'
        replace(origin, field)
        return fall_down(down, field)
    elif check(diag_left, field): #and not check_block(left,field):
        field[diag_left] = 'o'
        replace(origin, field)
        return fall_down(diag_left, field)
    elif check(diag_right, field): #and not check_block(right,field):
        field[diag_right] = 'o'
        replace(origin, field)
        return fall_down(diag_right, field)
    else:
        return 'rest'


ydim, xdim = field.shape
print(field.shape)
field = np.pad(field, (1,1), 'constant', constant_values='.')
f2 = np.pad(f2, (1,1), 'constant', constant_values='.')
#field[0,501-x0] = '+' #start_sand
st = tuple(np.where(field=='+'))
st2 = tuple(np.where(f2=='+'))
ct = 0
while True:
    #rc = fall_down(st, field)     
    rc = fall_down(st2, f2)
    ct += 1 
  #  if ct == 260:
 #       break
#    print(field[48:58,15:28])    
    if rc == 'bounds':
        break


conv = np.vectorize(ord)
#plotgrid = conv(field)
#print(st)
#ans = np.sum(field == 'o')
#print(ans)
plotgrid = conv(f2)
ans = np.sum(f2=='o')
print(ans)
plt.matshow(plotgrid)
plt.show()
#pdb.set_trace()
# answer: 436 is too low

with open('in.txt', 'r') as f:
    entry = f.readlines()

X = 1
cycle = 0
ans = list()
for ix, line in enumerate(entry):
    line = line.strip().split()
    op = line[0]
    if op == 'addx':
        for v in range(0,2):
            cycle += 1
            if cycle != 0 and cycle%20 == 0:
                ans.append(X * cycle) 
            if v == 1:
                X += int(line[1])
            #X += int(line[1]) if v == 1 else X ##doesn't work and don't know why
    elif op == 'noop':
        cycle += 1
        if cycle%20 == 0:
            ans.append(X * cycle)
    if cycle >= 220:
        print("ans {} cycle {}".format(ans,cycle))
        break
sol = ans[0]+ans[2]+ans[4]+ans[6]+ans[8]+ans[10]
print(sol)

##### PART 2 #####
X = 1
cycle = 0
sprite = [X,X+1,X+2]
CRT = list()

def add_crt(i, sprite, CRT):
    if i in sprite:
        CRT.append('#')
    else:
        CRT.append('.')

def reset(CRT, cycle, X, crt_list, sprite):
    crt_list.append(CRT)
    CRT = list()
    cycle = 0
    X = 1
    sprite = [X, X+1, X+2]
    return CRT, cycle, crt_list, sprite
        

crt_list = list()
for ix, line in enumerate(entry):
    line = line.strip().split()
    op = line[0]
    if op == 'addx':
        for v in range(0,2):
            cycle += 1
            add_crt(cycle,sprite,CRT)
            if len(CRT) == 40:
                CRT, cycle, crt_list, sprite = reset(CRT, cycle, X, crt_list, sprite)
                if len(crt_list) == 6:
                    break
            if v == 1:
                X += int(line[1])
                sprite = [X, X+1,X+2]
    elif op == 'noop':
        cycle += 1
        add_crt(cycle,sprite,CRT)
        if len(CRT) == 40:
            CRT, cycle, crt_list, sprite = reset(CRT, cycle, X, crt_list, sprite)
            if len(crt_list) == 6:
                break
for x in crt_list:
    print(x)

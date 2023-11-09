with open('in.txt', 'r') as f:
    entry = f.readlines()

folders = list()
current = None
mydict = {}
for line in entry:
    cmd = line.strip().split()
    if "$" in cmd and cmd[1] == 'cd':
        if cmd[2] == '/':
            if current is None:
                current = cmd[2]
            #current = cmd[2] if current is None
        elif cmd[2] != '/' and cmd[2] != '..':
            if current != "/":
                current += "/{}".format(cmd[2])
            else:
                current += cmd[2]
        elif cmd[2] == '..':
            current = '/'.join(current.split('/')[:-1])
            if current == '':
                current = '/' 
    
    if "$" in cmd and 'ls' in cmd:
        flag = True
        elements = list()
        size = 0
        mydict.update({current: []})
    elif "$" in cmd and 'ls' not in cmd:
        flag = False

    if flag and "$" not in cmd:
        if not cmd[0].isdigit():
            if current == '/':
                d = current + cmd[1]
            else:
                d = current + "/" + cmd[1]
            mydict[current].append(d)
        elif cmd[0].isdigit():
            mydict[current].append((int(cmd[0])))

print("----")
print(mydict)
def sum_values(mydict):
    for k,v in mydict.items():
        if isinstance(v,list):
            if all([isinstance(x,int) for x in v]):
                mydict[k] = sum(v)

    
def replace(mydict):
    for k,v in mydict.items():
        if isinstance(v,list):
            for i,ele in enumerate(v):
                if isinstance(ele,str):
                    if isinstance(mydict[ele], list):
                        continue
                    elif isinstance(mydict[ele], int):
                        v[i] = mydict[ele]

def check(mydict):
    for k,v in mydict.items():
        if isinstance(v,list):
            return False
    return True

while not check(mydict):
    sum_values(mydict)
    replace(mydict)

print(mydict)

ans=0
for k,v in mydict.items():
    if mydict[k] <= 100000:
        ans += mydict[k]

print(ans) 
################PART 2########
totalsize = 70000000
minimum = 30000000
current = totalsize - mydict['/']
to_delete = minimum - current

print("to delete: {}".format(to_delete))
#pdb.set_trace()
cond = list()
for k,v in mydict.items():
    if k == '/':
        continue
    if mydict[k] >= to_delete:
        cond.append(mydict[k])

print(sorted(cond)[0:3])

import pdb
import ast
from itertools import zip_longest

def check(a,b):
    if a is None and type(b) == int:
        return "right"
    elif type(a) == int and b is None:
        return "wrong"
    elif a > b:
        return "wrong"
    elif a < b:
        return "right"


def compare(l1, l2):
    out = False    
    for a, b in zip_longest(l1,l2):
        if type(a) == type(b) == int:
            out = check(a,b)
        elif a is None and type(b) == int:
            out = check(a,b)
        elif type(a) == int and b is None:
            out = check(a,b)
        elif type(a) != type(b):
            temp = list()
            if isinstance(a, int) and isinstance(b, list):
                temp.append(a)
                out = compare(temp,b)
            elif isinstance(b,int) and isinstance(a,list):
                temp.append(b)
                out = compare(a,temp)
            elif type(a) == int and b is None:
                out = check(a,b)
            elif a is None and type(b) == int:
                out = check(a,b)
        elif type(a) == type(b) == list:
            if a == b:
                continue
            else:
                out = compare(a,b)
        if out:
            break    
    if not out:
        if len(l1) > len(l2):
            return "wrong"
        elif len(l1) < len(l2):
            return "right"
    return out


with open('in.txt', 'r') as f:
    entry = f.readlines()

container = list()
index = 0
idx = list()
wrg = list()
nth = list()
for line in entry:
    if line != '\n':
        line = ast.literal_eval(line.strip())
        container.append(line)
    if len(container) == 2:
        res = compare(container[0], container[1])
        index += 1
        if res == 'right':
            idx.append(index)
        elif res == 'wrong':
            wrg.append(index)
        else:
            nth.append(index)
            print(container)
            print("\n")
        container = list()

print("total: {}, rights: {}, wrongs: {}, diff: {}".format(index,len(idx), len(wrg), index-len(idx)-len(wrg)))
#print(idx)
#print(wrg)
print("index nothing: {}".format(nth))

print(sum(idx))

###### PART 2 #######

olist = [[[2]],[[6]], [1000]]
for line in entry:
    if line != '\n':
        line = ast.literal_eval(line.strip())
        #container.append(line)
        count = 0
        for ele in olist:
            ans = compare(line, ele)
            if ans == 'right':
                olist.insert(count,line)
                break
            else:
                count += 1

        
    #for if len(container) == 2:
    #    res = compare(container[0], container[1])
     #   index += 1
print("PART 2")
#print(olist)
idx1 = olist.index([[2]])+1
idx2 = olist.index([[6]])+1
print("Answer part 2: {}".format(idx1*idx2))


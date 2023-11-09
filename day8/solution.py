import numpy as np
with open('in.txt', 'r') as f:
    entry = f.readlines()

m = list()
for line in entry:
    line = list(line.strip())
    line = [int(x) for x in line]
    m.append(line)

m = np.array(m)
print(m.shape)
visible = m.shape[0]*2+m.shape[1]*2+-4
for x in range(1,m.shape[1]-1):
    for y in range(1,m.shape[0]-1):
        bottom = m[y+1:m.shape[1],x]
        top = m[0:y,x]
        right = m[y,x+1:m.shape[0]]
        left = m[y,0:x]
        tree = m[y,x]
        if all([tree > x for x in bottom]) or all([tree > x for x in top]) or all([tree > x for x in left]) or all([tree > x for x in right]):
            visible += 1

print(visible)
########PART2

def distance(val, sight):
    count = 0
    for x in sight:
        if x >= val:
            count += 1
            return count
        else:
            count += 1
    return count

ans = list()
for x in range(1,m.shape[1]-1):
    for y in range(1,m.shape[0]-1):
        bottom =  m[y+1:99,x]
        top = m[0:y,x]
        right = m[y,x+1:99]
        left = m[y,0:x]
        tree = m[y,x]
        left = left[::-1]
        top = top[::-1]
        score_top = distance(tree,top)
        score_left = distance(tree,left)
        score_bottom = distance(tree,bottom)
        score_right = distance(tree,right)
        score = score_top*score_bottom*score_right*score_left
        ans.append(score)

print(sorted(ans)[-1])

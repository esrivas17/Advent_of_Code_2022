from copy import deepcopy
import string
upper = list(string.ascii_uppercase)

with open('in.txt', 'r') as f:
    entry = f.readlines()

crates = list()
for x in range(1,10):
    crates.append(list())

for arrange in entry[:9]:
    cratelist = list()
    for idx, crate in enumerate(list(arrange)[1:-1:4]):
        if crate in upper:
            crates[idx].append(crate)

crates_2  = deepcopy(crates)

for x in entry[10:]:
    z = x.strip().split()
    move = int(z[1])
    f = int(z[3])
    to = int(z[5])
    taking = crates[f-1][:move]
    [crates[to-1].insert(0,x) for x in taking]
    del crates[f-1][:move]

ans = [x[0] for x in crates]
print(''.join(ans))

###############PART2
for x in entry[10:]:
    z = x.strip().split()
    move = int(z[1])
    f = int(z[3])
    to = int(z[5])
    taking = crates_2[f-1][:move]
    crates_2[to-1] = taking + crates_2[to-1]
    del crates_2[f-1][:move]

part2 = [x[0] for x in crates_2]
print(''.join(part2))

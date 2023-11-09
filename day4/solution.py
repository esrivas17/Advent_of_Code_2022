with open('in.txt', 'r') as f:
    assignments = f.readlines()

count = 0
for assign in assignments:
    ranges = [x.split("-") for x in assign.strip().split(",")]
    #print(ranges)   
    if int(ranges[0][0]) >= int(ranges[1][0]) and int(ranges[0][1]) <= int(ranges[1][1]):
        count += 1
        continue
    if int(ranges[1][0]) >= int(ranges[0][0]) and int(ranges[1][1]) <= int(ranges[0][1]):
        count += 1
        continue

print(count)

#PART2
ans = 0
for assign in assignments:
    rgs = [x.split("-") for x in assign.strip().split(",")]
    test = set(range(int(rgs[0][0]),int(rgs[0][1])+1)) & set(range(int(rgs[1][0]), int(rgs[1][1])+1))
    #if len(list(test)) == 0:
    if not list(test):
        continue
    else:
        ans += 1
print(ans)

#Alternatives for PART1
alt1 = 0
alt2 = 0
for assign in assignments:
    rgs = [x.split("-") for x in assign.strip().split(",")]
    test = set(range(int(rgs[0][0]),int(rgs[0][1])+1)) & set(range(int(rgs[1][0]), int(rgs[1][1])+1))
    #print(tt)
    if sorted(list(test)) == sorted(list(range(int(rgs[0][0]),int(rgs[0][1])+1))) or sorted(list(test)) == sorted(list(range(int(rgs[1][0]), int(rgs[1][1])+1))):
        alt1 += 1
    if len(list(test)) == len(list(range(int(rgs[0][0]),int(rgs[0][1])+1))) or len(test) == len(list(range(int(rgs[1][0]),int(rgs[1][1])+1))):
        alt2 += 1

print(alt1)
print(alt2)

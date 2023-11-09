tr = list()
fa = list()
c2 = 0
c3 = 0
for x in range(0,10000):
    t = x *19
    if t%23==0:
        c2 += 1
    else:
        c3 += 1

print(c2)
print(c3)

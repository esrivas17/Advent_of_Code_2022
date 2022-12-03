X = [l.strip() for l in open('in.txt')]
sp = list()

for elf in ('\n'.join(X)).split('\n\n'):
    z = 0
    for x in elf.split('\n'):
        z += int(x)
    sp.append(z)

print(max(sp))
print(sum(sorted(sp)[-3:]))

#for elf in ('xx'.join(X)).split('xxxx')


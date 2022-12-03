import string
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
keys = lower+upper

priorities = {}
for idx, key in enumerate(keys):
    priorities.update({key: idx+1})

with open('in.txt', 'r') as f:
    rucksacks = f.readlines()

answer = 0
for items in rucksacks:
    items = list(items.strip())
    first_compartment = items[:int(len(items)/2)]
    second_compartment = items[int(len(items)/2):]
    it = list(set(first_compartment) & set(second_compartment))
    #it = [item1 for item1 in set(first_compartment) for item2 in set(second_compartment) if item1==item2]
    answer += priorities[it[0]]

print(answer)

#PART2

part2 = 0
group = list()
for items in rucksacks:
    group.append(list(items.strip()))
    if len(group) == 3:
        it = list(set(group[0]) & set(group[1]) & set(group[2]))
        part2 += priorities[it[0]]
        group = list()
        continue
print(part2)

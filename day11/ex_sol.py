from ex import *
from math import floor

monkeys = [monkey_0, monkey_1, monkey_2, monkey_3]
#count = [len(m) for m in monkeys]
monkey_items = [0,0,0,0]

for x in range(0,20):
    for monkey_id,monkey in enumerate(monkeys):
        num_items = len(monkey)
        count_items(monkey_items, monkey_id, num_items)
        if monkey:
            for idx, item in enumerate(monkey):
                worry = operation(item,monkey_id)
                new_worry = floor(worry/3)
                test(new_worry, monkey_id, monkeys)
            monkeys[monkey_id] = monkeys[monkey_id][num_items:]
        
#    new_count = [len(m) for m in monkeys]
#    print(monkeys)
print(monkey_items)
#print(count)

##### PART 2 #####
items_part2 = [0,0,0,0]
monkeys_part2 = [monkey_0, monkey_1, monkey_2, monkey_3]
for x in range(0,20):
    for monkey_id,monkey in enumerate(monkeys_part2):
        num_items = len(monkey)
        count_items(items_part2, monkey_id, num_items)
        if monkey:
            for idx, item in enumerate(monkey):
                worry = operation(item,monkey_id)
                test(worry, monkey_id, monkeys_part2)
            monkeys_part2[monkey_id] = monkeys_part2[monkey_id][num_items:]

print(items_part2)

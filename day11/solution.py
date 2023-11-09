from entry import *
from math import floor 

monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
count = [len(m) for m in monkeys]
monkey_items = [0,0,0,0,0,0,0,0]

for x in range(0,20):
    for monkey_id,monkey in enumerate(monkeys):
        count_items(monkey_items, monkey_id, len(monkey))
        for item in monkey:
            if item:
                worry = operation(item,monkey_id)
                worry = floor(worry/3)
                test(worry, monkey_id, monkeys)
        monkeys[monkey_id] = monkeys[monkey_id][len(monkey):]

print(monkey_items)
ans = sorted(monkey_items)
print(ans[-2]*ans[-1])


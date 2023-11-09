from ex import *

##### PART 2 #####
items_part2 = [0,0,0,0]
monkeys_part2 = [monkey_0, monkey_1, monkey_2, monkey_3]
lcm = 1
for gg in [23,19,13,17]:
    lcm *= (lcm*gg)
j = 23*19*13*17

for x in range(0,10000):
    for monkey_id, monkey in enumerate(monkeys_part2):
        num_items = len(monkey)
        count_items(items_part2, monkey_id, num_items)
        if monkey:
            for idx, item in enumerate(monkey):
                worry = operation(item,monkey_id)
                worry %= j
                test(worry, monkey_id, monkeys_part2)
            if monkeys_part2[monkey_id]:
                for n in range(num_items):        
                    monkeys_part2[monkey_id].pop(0)
            #monkeys_part2[monkey_id] = monkeys_part2[monkey_id][num_items:]

print(items_part2)

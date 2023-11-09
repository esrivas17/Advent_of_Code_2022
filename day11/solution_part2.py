from math import floor
from entry import *

######### PART2 #########
monkeys_part2 = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]
items = [0,0,0,0,0,0,0,0]

mcd = 5*17*2*7*3*11*13*19
print("mcd : {}".format(mcd))
for x in range(0,10000):
    for monkey_id,monkey in enumerate(monkeys_part2):
        count_items(items, monkey_id, len(monkey))
        for item in monkey:
            if item:
                worry = operation(item,monkey_id)
                worry %= mcd # it works but why?
                test(worry, monkey_id, monkeys_part2)
        monkeys_part2[monkey_id] = monkeys_part2[monkey_id][len(monkey):]

print(items)
ans_part2 = sorted(items)
print(ans_part2[-2]*ans_part2[-1])

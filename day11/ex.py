monkey_0 = [79, 98]

monkey_1 = [54, 65, 75, 74]

monkey_2 = [79, 60, 97]

monkey_3 = [74]


def operation(old, monkey_id):
    if monkey_id == 0:
        return old*19
    elif monkey_id == 1:
        return old+6
    elif monkey_id == 2:
        return old*old
    elif monkey_id == 3:
        return old+3
    else:
        return None

def test(item, monkey_id, monkeys):
    if monkey_id == 0:
        if item%23 == 0:
            monkeys[2].append(item)
        else:
            monkeys[3].append(item)
    if monkey_id == 1:
        if item%19 == 0:
            monkeys[2].append(item)
        else:
            monkeys[0].append(item)
    if monkey_id == 2:
        if item%13 == 0:
            monkeys[1].append(item)
        else:
            monkeys[3].append(item)
    if monkey_id == 3:
        if item%17 == 0:
            monkeys[0].append(item)
        else:
            monkeys[1].append(item)

def count_items(c_list, idx, num):
    c_list[idx] += num
    

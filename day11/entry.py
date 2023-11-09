monkey_0 = [77,69,76,77,50,58]

monkey_1 = [75, 70, 82, 83, 96, 64, 62]

monkey_2 = [53]

monkey_3 = [85, 64, 93, 64, 99]

monkey_4 = [61, 92, 71]

monkey_5 = [79, 73, 50, 90]

monkey_6 = [50, 89]

monkey_7 = [83, 56, 64, 58, 93, 91, 56, 65]

def operation(old, monkey_id):
    if monkey_id == 0:
        return old*11
    elif monkey_id == 1:
        return old+8
    elif monkey_id == 2:
        return old*3
    elif monkey_id == 3:
        return old+4
    elif monkey_id == 4:
        return old*old
    elif monkey_id == 5:
        return old+2
    elif monkey_id == 6:
        return old+3
    elif monkey_id == 7:
        return old+5
    else:
        return None

def test(item, monkey_id, monkeys):
    if monkey_id == 0:
        if item%5 == 0:
            monkeys[1].append(item)
        else:
            monkeys[5].append(item)
    if monkey_id == 1:
        if item%17 == 0:
            monkeys[5].append(item)
        else:
            monkeys[6].append(item)
    if monkey_id == 2:
        if item%2 == 0:
            monkeys[0].append(item)
        else:
            monkeys[7].append(item)
    if monkey_id == 3:
        if item%7 == 0:
            monkeys[7].append(item)
        else:
            monkeys[2].append(item)
    if monkey_id == 4:
        if item%3 == 0:
            monkeys[2].append(item)
        else:
            monkeys[3].append(item)
    if monkey_id == 5:
        if item%11 == 0:
            monkeys[4].append(item)
        else:
            monkeys[6].append(item)
    if monkey_id == 6:
        if item%13 == 0:
            monkeys[4].append(item)
        else:
            monkeys[3].append(item)
    if monkey_id == 7:
        if item%19 == 0:
            monkeys[1].append(item)
        else:
            monkeys[0].append(item)


def count_items(c_list, idx, num):
    c_list[idx] += num

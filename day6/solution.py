with open('in.txt', 'r') as f:
    entry = f.readlines()

entry = list(entry[0].strip())
check = list()
for ix, cha in enumerate(entry):
    #print("{} {}".format(check, ix))
    if len(check) < 4:
        check.append(cha)
    elif len(check) == 4:
        if len([x for x in check if check.count(x) == 1]) ==4:
            print(ix)
            break
        else:
           check.append(cha)
           check = check[-4:]
  
################PART2
for ix, cha in enumerate(entry):
    if len(check) < 14:
        check.append(cha)
    elif len(check) == 14:
        if len([x for x in check if check.count(x) == 1]) == 14:
            print(ix)
            break
        else:
            check.append(cha)
            check = check[-14:]

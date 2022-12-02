with open('in.txt', 'r') as f:
    elves_list = f.readlines()

number_calories = list()

count = 0
for calories in elves_list:
    try:
        int(calories)
    except:
        number_calories.append(count)
        count = 0
        continue
    else:
        count += int(calories)

#getting max
max_calories = max(number_calories)
ix = number_calories.index(max_calories)
#idx = [x for x, v in enumerate(number_calories) if v==max_calories]
print("Index of max value is: {} and value: {}".format(ix,max_calories))

##part2
sorted_number_calories = sorted(number_calories, reverse=True)
solution = sum(sorted_number_calories[0:3])
print("sum of 3 first elves with most calories: {}".format(solution))

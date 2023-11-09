with open('in.txt', 'r') as f:
    guide = f.readlines()


def rock_paper_scissors(entry1, entry2) -> int:
    if entry1 == entry2:
        return 3
    if entry1 == 'rock' and entry2 == 'paper':
        return 6
    if entry1 == 'rock' and entry2 == 'scissors':
        return 0
    if entry1 == 'paper' and entry2 == 'rock':
        return 0
    if entry1 == 'paper' and entry2 == 'scissors':
        return 6
    if entry1 == 'scissors' and entry2 == 'rock':
        return 6
    if entry1 == 'scissors' and entry2 == 'paper':
        return 0


def score_shape(entry) -> int:
    mydict = {'rock': 1, 'paper': 2, 'scissors': 3}
    return mydict[entry]


def convert_entries(in1, in2):
    mydict = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    return mydict[in1], mydict[in2]


total_score = 0
for line in guide:
    elf_entry, me_entry = line.strip().split(" ")
    elf, myself = convert_entries(elf_entry, me_entry)
    shape_score = score_shape(myself)
    game_score = rock_paper_scissors(elf, myself)
    round_score = shape_score + game_score
    total_score += round_score

print("Total score is: {}".format(total_score))

##PART 2###
def entry_to_use(in1, outcome):
    choices = ['rock', 'paper', 'scissors']
    if outcome == 'Y':
        return in1
    if outcome == 'X':
        for choice in choices:
            score = rock_paper_scissors(in1, choice)
            if score == 0:
                return choice
    if outcome == 'Z':
        for choice in choices:
            score = rock_paper_scissors(in1, choice)
            if score == 6:
                return choice


def evaluate_outcome(outcome) -> int:
    mydict = {'X': 0, 'Y': 3, 'Z': 6}
    return mydict[outcome]


total_score_part2 = 0

for line in guide:
    elf_entry, outcome = line.strip().split(" ")
    elf, _ = convert_entries(elf_entry, outcome)
    mychoice = entry_to_use(elf, outcome)
    score1 = score_shape(mychoice)
    score2 = evaluate_outcome(outcome)
    total_score_part2 += score1 + score2

print("Result part2 is: {}".format(total_score_part2))

with open('in.txt', 'r') as f:
    entry = f.readlines()

def get_rank(l):
    if type(l[0]) == int:
return l[0]
elif type(l[0]) == list:
if len


for line in entry:
    if line != '\n':
        line = ast.literal_eval(line.strip())
        container.append(line)

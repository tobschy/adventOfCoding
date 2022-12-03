import string

def getPriority(character):
    priority = string.ascii_lowercase + string.ascii_uppercase
    return priority.find(character)+1


def getGroups(file: string):
    with open(file) as data:
        lines = data.readlines()
        return [lines[x:x+3] for x in range(0,len(lines),3)]


prioritySum = 0
groups = getGroups('data.txt')
for group in groups:
    for char in group[0].strip():
        if (char in group[1]) and (char in group[2]):
            prioritySum += getPriority(char)
            break    

print(prioritySum)

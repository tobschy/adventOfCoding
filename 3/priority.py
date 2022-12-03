import string

def getPriority(character):
    priority = string.ascii_lowercase + string.ascii_uppercase
    return priority.find(character)+1


prioritySum = 0
with open('data.txt') as data:
    for line in data.readlines():
        line = line.strip()
        compBreak = int(len(line)/2)
        compartment1 = line[0:compBreak]
        compartment2 = line[-compBreak:]
        for char in compartment1:
            if char in compartment2:
                prioritySum += getPriority(char)
                break

print(prioritySum)

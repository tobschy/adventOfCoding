score = 0
scoreBySelect = {'X': 1, 'Y': 2, 'Z': 3}

win = {"A":"A Y", "B":"B Z", "C":"C X"}
draw = {"A":"A X", "B":"B Y", "C":"C Z"}
loose = {"A":"A Z", "B":"B X", "C":"C Y"}

strategy = {"X": loose, "Y": draw, "Z": win}

with open('data.txt') as data:
    lines = data.readlines()
    for line in lines:
        line = line.strip()
        line = strategy[line[-1]][line[0]]
        score += scoreBySelect[line[-1]]
        if line == win[line[0]]:
            score += 6
        else:
             if line == draw[line[0]]:
                score += 3

print(score)
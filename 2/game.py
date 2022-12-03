score = 0
scoreBySelect = {'X': 1, 'Y': 2, 'Z': 3}
#strategy = {"X": loose, "Y": draw, "Z": win}

win = ["A Y", "B Z", "C X"]
draw = ["A X", "B Y", "C Z"]
loose = ["A Z", "B X", "C Y"]

with open('data.txt') as data:
    lines = data.readlines()
    for line in lines:
        line = line.strip()
        score += scoreBySelect[line[-1]]
        if line in win:
            score += 6
        else:
             if line in draw:
                score += 3
        

print(score)
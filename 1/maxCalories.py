maxCalories = 0
calories = 0
caloriesPerElve = []

with open('data.txt') as data:
    lines = data.readlines()
    for line in lines:
        if line == '\n':
            caloriesPerElve.append(calories)
            calories = 0
        else:
            calories += int(line)

print(f"max Calories: {max(caloriesPerElve)}")
print(sum(sorted(caloriesPerElve)[-3:]))
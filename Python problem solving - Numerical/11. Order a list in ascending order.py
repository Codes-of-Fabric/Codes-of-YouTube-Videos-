
numbers = [8, 2, 1, 7, 5, 6, 3, 4]

for item1 in range(len(numbers)):
    for item2 in range(item1 + 1, len(numbers)):
        if numbers[item1] > numbers[item2]:
           numbers[item1], numbers[item2] = numbers[item2], numbers[item1]

print(numbers)

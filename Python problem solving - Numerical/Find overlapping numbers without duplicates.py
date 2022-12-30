
numbers_1 = [1, 2, 2, 3, 7, 8, 10, 12, 14]
numbers_2 = [1, 2, 3, 3, 4, 5, 6, 8, 8, 10]

common_numbers = []

for item in set(numbers_1):
    if item in numbers_2:
        common_numbers.append(item)

print(common_numbers)
        
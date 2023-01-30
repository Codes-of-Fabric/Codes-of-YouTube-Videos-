numbers = [1, 2, 3, 4, [5, 6, 7], 8, 9, 10]
name = 'Mount Everest is the tallest'
numbers_set = {11, 12, 13, 14}

print(numbers.index(10))
print(numbers[-2])
print(numbers[4][1])

print(name.index('t', 5))
print(name[-3])

for position, element in enumerate(numbers):
    print(position, element)

print(numbers.index(20))

numbers_set[0]
print(list(numbers_set)[0])

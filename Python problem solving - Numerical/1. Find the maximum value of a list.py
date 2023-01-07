
numbers = [2, 4, 5, 16, 8, 9, 7, 3]

def findmax(numbers):
    maximum = numbers[0]
    for item in numbers:
        if item > maximum:
            maximum = item
    return maximum  

findmax(numbers)     

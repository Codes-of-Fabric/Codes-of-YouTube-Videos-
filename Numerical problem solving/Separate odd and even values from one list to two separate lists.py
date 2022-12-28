
numbers = [-13, 2, 3, 4, 7, 11, 12]

def separate_odd_even(input_list):
    odd = []
    even = []
    for item in input_list:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    return odd, even

separate_odd_even(numbers)


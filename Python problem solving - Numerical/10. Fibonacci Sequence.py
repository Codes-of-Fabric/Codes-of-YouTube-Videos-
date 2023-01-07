# Fibonacci Sequence:  0, 1, 1, 2, 3, 5, 8, 13

def fibonacci_sequence(input_number):
    number_1 = 0
    number_2 = 1
    count = 0
    
    if input_number <= 0:
        print("Not a positive integer")
    elif input_number == 1:
        print(number_1)
    else:
        while count < input_number:
            print(number_1)
            fib_number = number_1 + number_2 # 1,2 of current window
            number_1 = number_2              # 1 of next window
            number_2 = fib_number            # 2 of next window
            count += 1

fibonacci_sequence(4)


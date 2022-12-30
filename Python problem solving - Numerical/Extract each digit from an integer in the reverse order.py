
number = 12345

# Using a for loop
for item in str(number)[::-1]:
    print(item, end=" ")

# Using a while loop
while number > 0:
    digit = number % 10
    print(digit, end=" ")
    number = number // 10



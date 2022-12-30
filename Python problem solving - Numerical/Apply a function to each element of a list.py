
numbers = [2, 3, 4, 5, 6]

# Using a for loop
new_numbers = []

for item in numbers:
    new_value = item*3 + 5
    new_numbers.append(new_value)
print(new_numbers)
  
# Using a lambda function
function = lambda x: 3*x + 5

output = [*map(function, numbers)]
print(output)


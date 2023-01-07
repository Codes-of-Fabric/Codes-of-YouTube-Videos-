
favorites = ['banana', 'apple', 'peach', 'cabbage', 'orange']

# For loop
fruits = []

for item in favorites:
    if item != 'cabbage':
        fruits.append(item)
print(fruits)

# Lambda function
function = lambda item: item!= 'cabbage'

fruits_only = list(filter(function, favorites))
print(fruits_only)

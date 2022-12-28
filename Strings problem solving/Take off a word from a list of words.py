

favorites = ['banana', 'apple', 'peach', 'potato', 'orange']

fruits = []

for item in favorites:
    if item != 'potato':
        fruits.append(item)

print(fruits)

# Write a lambda fucntion too
function = lambda x: x!= 'potato'

result = (*map(fucntion, favorites))
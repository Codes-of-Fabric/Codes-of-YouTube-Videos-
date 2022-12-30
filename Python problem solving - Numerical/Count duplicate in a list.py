
fruits = ['Banana','Mango','Kiwi','Grapes','Mango','Grapes','Orange']

# Find duplicates elements
duplicates = set()

for item in fruits:
    if (fruits.count(item) > 1):
        duplicates.add(item)
print(duplicates)    

# Count each element
elements_count = {}

for item in fruits:
    elements_count[item] = fruits.count(item) # key, value
print(elements_count)
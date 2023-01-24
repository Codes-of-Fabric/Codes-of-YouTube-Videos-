'''Iteration - Taking one element at a time from a 
               collection of elements'''

# Iterable
numbers = [1, 2, 3, 4]
name = 'Jupiter'
marks = {'A':10, 'B':20, 'C':30}

height = 155 # Not an iterable

# Iterator
for item in numbers:
    print(item)
   
# Iteration
for item in numbers:     # Iterable - numbers
    print(item * 2 + 1)  # Iterator - For loop    

for key,value in marks.items():
    print(value)

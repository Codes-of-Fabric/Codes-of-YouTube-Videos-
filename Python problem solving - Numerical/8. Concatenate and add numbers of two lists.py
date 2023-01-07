numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 8]

# Concatenate
joined_list = numbers_1 + numbers_2
print(joined_list)

# Add element-wise
sum_list = []
for item1, item2 in zip(numbers_1, numbers_2):
    sum_list.append(item1 + item2)
print(sum_list) 

   

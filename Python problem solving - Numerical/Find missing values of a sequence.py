
sequence = [1, 3, 5, 9, 11, 13, 15]

start = sequence[0]
end = sequence[-1]
step = sequence[1] - sequence[0]

for item in range(start, end+step, step):
    if item not in sequence:
        print(item)
      

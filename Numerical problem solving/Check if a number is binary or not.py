
number = 100102

def binarycheck(number):
    number = str(number)
    binary_characters = '01'
    not_binary = 0
    for element in number:
        if element not in binary_characters:
            not_binary = 1
            break
        else:
            pass
            
    if not_binary: 
        return("No") 
    else : 
        return("Yes")

binarycheck(number)



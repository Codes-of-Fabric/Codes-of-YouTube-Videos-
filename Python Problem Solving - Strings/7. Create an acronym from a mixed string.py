
name = 'urban volleyball club 78'

words = name.split(' ')

letters = ''
numbers = ''

for item in words:
    if item.isalpha():
        letters += item[0].upper()
    else: 
        numbers += item
      
acronym = " ".join([letters, numbers])
 
    

sentence = '''Jonna James is married to Jimmy Jones Jr. 
for 50 years, and they are the happiest couple ever!!!'''

words = sentence.split(' ')

word_length = []
for word in words:
    word_replace = word.replace('\n', '')
    word_strip = word_replace.rstrip(',.!')
    word_length.append(len(word_strip))

average_length = (sum(word_length)/len(word_length))
print(round(average_length))
    

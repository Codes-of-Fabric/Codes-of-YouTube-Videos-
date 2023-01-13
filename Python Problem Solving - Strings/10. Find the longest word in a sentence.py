
sentence = 'She made a delicious ginger bread'

words = sentence.split(' ')

longest_word = max(words, key=len)

print(longest_word)

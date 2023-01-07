
input_words = ["aaa123", "bbb2rs3", "ccc456nmo7pq8", "ddefg"]

digits_count = 0
digits_per_word = {}
for word in input_words:
    for character in word:
        if character.isdigit():
            digits_count += 1
        else:
            pass
    digits_per_word[word] = digits_count
    digits_count = 0
            
print(digits_per_word)

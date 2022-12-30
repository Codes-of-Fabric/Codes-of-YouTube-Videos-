
sentence = "I love watermelon"

def extract_vowels(sentence):
    vowels = "aeiou"
    vowels_in_sentence = '' 
    for letter in sentence:
        if letter in vowels:
            vowels_in_sentence = vowels_in_sentence + letter
    return vowels_in_sentence

extract_vowels(sentence)

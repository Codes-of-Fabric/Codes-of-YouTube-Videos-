#Insert a new letter at the middle of a sentence

def insert_letter(word, letter):
    letter = str(letter)
    word_length = len(word)
    mid_point = int(word_length/2)
    new_word = word[:mid_point]+ str(letter) +word[mid_point:]
    return(new_word)

insert_letter('Watermelon', 1)

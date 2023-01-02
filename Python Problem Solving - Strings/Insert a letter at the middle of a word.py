
def insert_letter(word, letter):
    word_length = len(word)
    mid_point = int(word_length/2)
    new_word = word[:mid_point]+ letter + word[mid_point:]
    return(new_word)

insert_letter('Jubo', 'm')



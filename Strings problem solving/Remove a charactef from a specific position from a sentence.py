#Remove the character at nth index from a string

sentence = 'I love a chocolate'

def remove_character(sentence, position):
    input_string = sentence
    string_1 = input_string[0:position]
    string_2 = input_string[position+1:]
    output_string = string_1 + string_2
    return(output_string)

remove_character(sentence, 3)


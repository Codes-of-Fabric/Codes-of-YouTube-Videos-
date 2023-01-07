
input_word = "brother"

def count_characters(input_string):
    character_dict = dict()
    for character in input_string:
        count = input_string.count(character)
        character_dict[character] = count
    return character_dict

count_characters(input_word)

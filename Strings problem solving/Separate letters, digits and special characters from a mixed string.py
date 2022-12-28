#!/usr/bin/env python3

import re

sentence = 'Price of my car:15000$'
numbers = re.findall("\d", sentence)
print(numbers)

letters = re.findall("[a-zA-Z]", sentence)
print(letters)

special_characters = re.findall("[^a-zA-Z0-9\s]", sentence)
print(special_characters)

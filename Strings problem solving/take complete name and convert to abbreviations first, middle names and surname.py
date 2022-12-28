
full_names = ["Mark Elliot White", "George Dolton"]
abbreviate_name =[]

for item in full_names:
    item = item.split()
    initials = ''
    for name in item[::-1][1:]:
        initials+= name[0]

    initials_concat =".".join(map(str,initials[::-1]))
    name_initials = initials_concat + '.' + item[-1]
    abbreviate_name.append(name_initials)         

print(abbreviate_name)

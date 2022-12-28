soccer_players = ['John Terry','Roberto Carlos', 'Didier Drogba']

# Using for loops
surnames = []
for player in soccer_players:
    surname = player.split(' ')[-1]
    surnames.append(surname)
surnames.sort()
print(surnames)

sorted_surname = []
for player in soccer_players:
    for surname in surnames:
        if surname in player:
            sorted_surname.append(player)
print(sorted_surname)

# Using lambda function 
soccer_players.sort(key=lambda name: name.split(" ")[-1])
print(soccer_players)

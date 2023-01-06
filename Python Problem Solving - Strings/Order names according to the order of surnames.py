soccer_players = ['John Terry','Roberto Carlos', 'Didier Drogba']

# Using for loops
surnames = []
for player in soccer_players:
    surname = player.split(' ')[-1]
    surnames.append(surname)
surnames.sort()

sorted_names = []
for surname in surnames:
    for player in soccer_players:
        if surname in player:
            sorted_names.append(player)
print(sorted_names)

# Using lambda function 
soccer_players.sort(key=lambda name: name.split(" ")[-1])
print(soccer_players)

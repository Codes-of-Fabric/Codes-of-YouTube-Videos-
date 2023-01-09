
winners = ['1930 - Uruguay','1934 - Italy','1938 - Italy','1950 - Uruguay',
           '1954 - West Germany','1958 - Brazil','1962 - Brazil','1966 - England',
           '1970 - Brazil','1974 - West Germany','1978 - Argentina','1982 - Italy',
           '1986 - Argentina','1990 - West Germany','1994 - Brazil','1998 - France',
           '2002 - Brazil','2006 - Italy','2010 - Spain','2014 - Germany',
           '2018 - France','2022 - Argentina']

countries = []

for winner in winners:
    countries.append(winner.split(' - ')[-1])
    
print(countries)

print(*enumerate(countries))

for position, country in enumerate(countries):
    if country == 'Argentina':
        print(position + 1)
















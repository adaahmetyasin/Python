from random import shuffle

notp = int(input("enter the number of team players: "))

players_names = []

for i in range(notp):
    i = input("enter players' names: ")
    players_names.append(i)

shuffle(players_names)

nott = int(input("enter the number of teams: "))


btks = notp / nott

for i in range(notp):
    print(players_names[i])
    if (i+1) % btks == 0:
        print(" ")
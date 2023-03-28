import getpass
import random
import math

round_number = int(input('Ilość rund> '))
player_count = int(input('Ilość graczy(1,2)> '))
names_of_players = [input('Nazwa gracza 1> '), input('Nazwa gracza 2> ')]
games = []
print("Początek gry!")
for i in range(1, round_number + 1):
    print("Runda " + str(i))
    player_one_choice = getpass.getpass('{}(p,k,n)> '.format(names_of_players[0]))
    player_two_choice = None
    if not (player_one_choice == 'p' or player_one_choice == 'k' or player_one_choice == 'n'):
        print("Naucz się grać!")
        exit(1)
    if player_count == 1:
        player_two_choice = random.choice(['p', 'k', 'n'])[0]
    else:
        player_two_choice = getpass.getpass('{}(p,k,n)> '.format(names_of_players[1]))
        if not (player_two_choice == 'p' or player_two_choice == 'k' or player_two_choice == 'n'):
            print("Naucz się grać!")
            exit(1)
    games.append([player_one_choice, player_two_choice, i])

score = 0
for game in games:
    if game[0] == 'p':
        if game[1] == 'p':
            continue
        elif game[1] == 'k':
            score += 1
        else:
            score -= 1
    elif game[0] == 'k':
        if game[1] == 'k':
            continue
        elif game[1] == 'n':
            score += 1
        else:
            score -= 1
    elif game[0] == 'n':
        if game[1] == 'n':
            continue
        elif game[1] == 'p':
            score += 1
        else:
            score -= 1
print("Gry:")
for game in games:
    print(str(game[2]) + ": " + str(game[0]) + " vs " + str(game[1]))
if score > 0:
    print(names_of_players[0] + " wygrał")
elif score < 0:
    print(names_of_players[1] + " wygrał")
else:
    print("Remis")

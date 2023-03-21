import getpass
import random

round_number = int(getpass.getpass('Ilość rund(3)> '))
player_count = int(getpass.getpass('Ilość graczy(1)> '))
names_of_players = [getpass.getpass('Nazwa gracza 1> '), getpass.getpass('Nazwa gracza 2> ')]
games = []
print("Początek gry!")
for i in range(0, round_number):
    player_one_choice = getpass.getpass('{}(p,k,n)> '.format(names_of_players[0]))
    if player_one_choice == 'p' or player_one_choice == 'k' or player_one_choice == 'n':
        pass
    else:
        print("Naucz się grać!")
        exit(1)
    if player_count == 1:
        pass
    else:
        pass

# 1. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint as rnd

total_candies = 2021
max_candies = 28


def take_candy(player):
    candies = 0
    while candies < 1 or candies > max_candies:
        candies = int(input(f'{player}, take from 1 to {max_candies} candies: '))
    return candies


print('*** Candy game ***')
mode = -1
while not (mode == 1 or mode == 2):
    mode = int(input('Enter play mode (1 - Person VS Person | 2 - Person VS Computer): '))

difficulty = -1
if mode == 2:
    while not (difficulty == 0 or difficulty == 1):
        difficulty = int(input('Select difficulty (0 - NORMAL | 1 - HARD): '))

player1 = 'Player1'
player2 = 'Player2' if mode == 1 else 'Bot'
first_move = rnd(0, 1)
print(f'{player1 if first_move == 0 else player2} takes first.')

remaining_candies = total_candies
while remaining_candies > max_candies:
    candies = 0
    if first_move == 0:
        candies = take_candy(player1)
    else:
        if mode == 1:  # Person VS Person
            candies = take_candy(player2)
        else:  # Person VS Computer
            if difficulty == 0:  # NORMAL
                candies = rnd(1, max_candies)
            else:  # HARD
                candies = remaining_candies % (max_candies + 1)
                if candies == 0:
                    candies = rnd(1, max_candies)

            print(f'{player2} took {candies} candies.')

    remaining_candies -= candies

    print(f'Remaining candies: {remaining_candies}.')

    if first_move == 0:
        first_move += 1
    else:
        first_move -= 1

print(f'{player1 if first_move == 0 else player2} wins!')

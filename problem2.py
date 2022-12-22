# 2. Создайте программу для игры в ""Крестики-нолики"".

from random import randint as rnd


def create_moves_indexes():
    indexes = dict()
    for i in range(len(winning_series)):
        for j in range(len(winning_series[i])):
            if winning_series[i][j] in indexes:
                indexes[winning_series[i][j]].append((i, j))
            else:
                indexes[winning_series[i][j]] = [(i, j)]
    return indexes


def print_playground():
    for i in range(3):  # take only first three lists to draw a playground
        for j in range(len(winning_series[i])):
            print(str(winning_series[i][j]), end='\n' if j == len(winning_series[i])-1 else ' | ')


def make_move():
    flag = True
    while flag:
        n = int(input(f'{player1 if first_move == 0 else player2}, where to put your "{mark}" (1 - 9)? '))
        if 0 < n < 10 and n not in marked_areas:
            marked_areas.append(n)
            mark_position(n)
            flag = False
        else:
            print('Invalid input!')


def mark_position(position: int):
    for i in moves_indexes[position]:
        winning_series[i[0]][i[1]] = mark


# return:
# -1 -draw
#  0 -keep playing
#  1 -winner
def get_result():
    i = 0
    iter_series = True
    total_marks = 0
    while iter_series and i < len(winning_series):
        cur_mark = ''
        mark_count = 0
        iter_sequence = True
        j = 0
        while iter_sequence and j < len(winning_series[i]):
            if winning_series[i][j] != 'O' and winning_series[i][j] != 'X':
                iter_sequence = False
            else:
                if cur_mark == '':
                    cur_mark = winning_series[i][j]
                    mark_count = 1
                elif cur_mark == winning_series[i][j]:
                    mark_count += 1
                    if mark_count == 3:
                        return 1

                total_marks += 1
                j += 1

        i += 1

    if total_marks == 24:
        return -1

    return 0


print('*** Tic-Tac-Toe ***')
winning_series = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
moves_indexes = create_moves_indexes()  # create indexes for play fields for faster search
marked_areas = list()

player1 = 'Player1'
player2 = 'Player2'
first_move = rnd(0, 1)

print(f'{player1 if first_move == 0 else player2} plays first.')
mark = ''
while not (mark.upper() == 'O' or mark.upper() == 'X'):
    mark = input(f'{player1 if first_move == 0 else player2}, select your mark ("O" OR "X"): ')
mark = mark.upper()

keep_playing = True
while keep_playing:
    print_playground()
    make_move()
    result = get_result()

    if result == 1:
        keep_playing = False
        print(f'{player1 if first_move == 0 else player2} ({mark}) wins!')
    elif result == -1:
        keep_playing = False
        print("It's a draw!")
    else:
        if first_move == 0:
            first_move += 1
        else:
            first_move -= 1

        mark = 'X' if mark == 'O' else 'O'

print()
print('Game Over')
print_playground()

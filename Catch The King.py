from random import randint


def player_choice(player):
    now_is = 'White' if player == 'W' else "Black"
    while True:
        try:
            person = int(input(f'{now_is}, please choose a number between 1 and {8}:\n'))
            if 1 <= person <= 8:
                return person - 1
            else:
                print('Please enter a valid number!')
        except ValueError:
            print('Invalid values, try again!')


size = 8
board = [['_'] * size for _ in range(size)]

mapper = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up_left': lambda r, c: (r - 1, c - 1),
    'up_right': lambda r, c: (r - 1, c + 1),
    'down_left': lambda r, c: (r + 1, c - 1),
    'down_right': lambda r, c: (r + 1, c + 1)
}

numbers_of_the_commands = {
    0: 'up',
    1: 'down',
    2: 'left',
    3: 'right',
    4: 'up_left',
    5: 'up_right',
    6: 'down_left',
    7: 'down_right'
}

white_row = 0
white_col = 0
black_row = 7
black_col = 7
king_row = randint(0, size - 1)
king_col = randint(0, size - 1)

board[white_row][white_col] = 'W'
board[black_row][black_col] = 'B'
board[king_row][king_col] = 'K'

current_player, second_player = 'W', 'B'
iteration = 0
for row in board:
    print(row)

while True:
    current_player_choice = player_choice(current_player)
    direction = numbers_of_the_commands[current_player_choice]

    if current_player == 'W':
        board[white_row][white_col] = '_'
        next_row, next_col = mapper[direction](white_row, white_col)
        next_row = next_row % size
        next_col = next_col % size

        if board[next_row][next_col] == 'K':

            winner = "White" if current_player == "W" else "Black"
            board[next_row][next_col] = current_player
            for row in board:
                print(row)
            print(f'The King has been captured on position ({next_row}, {next_col})! {winner} won!')
            break

        elif board[next_row][next_col] == 'B':
            print('You can not stand on the enemy position!')
            continue

        board[next_row][next_col] = current_player
        white_row, white_col = next_row, next_col
    else:
        board[black_row][black_col] = '_'
        next_row, next_col = mapper[direction](black_row, black_col)
        next_row = next_row % size
        next_col = next_col % size

        if board[next_row][next_col] == 'K':

            winner = "White" if current_player == "W" else "Black"
            board[next_row][next_col] = current_player
            for row in board:
                print(row)
            print(f'The King has been captured on position ({next_row}, {next_col})! {winner} won!')
            break

        elif board[next_row][next_col] == 'W':
            print('You can not stand on the enemy position!')
            continue

        board[next_row][next_col] = current_player
        black_row, black_col = next_row, next_col

    current_player, second_player = second_player, current_player
    iteration += 1

    if iteration == 5:
        board[king_row][king_col] = '_'
        king_row = randint(0, size - 1)
        king_col = randint(0, size - 1)
        board[king_row][king_col] = 'K'
        iteration = 0

    for row in board:
        print(row)

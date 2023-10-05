from random import randint

# Constants
SIZE = 8
MAX_ITERATIONS = 20

direction = {
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up_left': lambda r, c: (r - 1, c - 1),
    'up_right': lambda r, c: (r - 1, c + 1),
    'down_left': lambda r, c: (r + 1, c - 1),
    'down_right': lambda r, c: (r + 1, c + 1)
}

get_name_of_the_command = {
    0: 'up',
    1: 'down',
    2: 'left',
    3: 'right',
    4: 'up_left',
    5: 'up_right',
    6: 'down_left',
    7: 'down_right'
}


def initialize_board():
    return [['_'] * SIZE for _ in range(SIZE)]


def print_board(board):
    for row in board:
        print(f"{'| '}{' | '.join(row)}{' |'}")


def player_choose_direction(player):
    now_is = 'White' if player == 'W' else 'Black'
    while True:
        try:
            person = int(input(f'{now_is}, please choose a number between 1 and {SIZE}: ')) - 1
            if 0 <= person < SIZE:
                return person
            else:
                print('Please enter a valid number!')
        except ValueError:
            print('Invalid values, try again!')


def move_player(board, player, row, col):
    is_the_king_captured = False

    if 0 <= row < SIZE and 0 <= col < SIZE:
        if board[row][col] == 'K':
            board[row][col] = player
            is_the_king_captured = True

        elif board[row][col] == '_':
            board[row][col] = player
        else:
            return 'Busy Position'

        return is_the_king_captured  # Returns True when the player catch the King or False when he can't.
    else:
        print('Invalid move. Stay on the board!')


def set_next_row_and_column(sel_dir, o_row, o_col):
    row, col = direction[sel_dir](o_row, o_col)

    # Here I use modulo division. That allows the player to get back on the board when he goes outside of it.
    row %= SIZE
    col %= SIZE

    return row, col


def the_king_is_captured(board, curr_player, n_row, n_col, o_row, o_col):
    board[o_row][o_col] = '_'
    print_board(board)
    winner = 'White' if curr_player == 'W' else 'Black'
    print(f'The King has been captured on position ({n_row}, {n_col}). {winner} wins!')

    return winner


def main():
    board = initialize_board()

    white_row, white_col = 0, 0
    black_row, black_col = SIZE - 1, SIZE - 1
    king_row, king_col = randint(1, SIZE - 2), randint(0, SIZE - 1)

    board[white_row][white_col] = 'W'
    board[black_row][black_col] = 'B'
    board[king_row][king_col] = 'K'

    current_player, second_player = 'W', 'B'
    iteration = 0

    while iteration < MAX_ITERATIONS:
        print_board(board)

        old_row = white_row if current_player == 'W' else black_row
        old_col = white_col if current_player == 'W' else black_col

        selected_direction = get_name_of_the_command[player_choose_direction(current_player)]

        next_row, next_col = set_next_row_and_column(selected_direction, old_row, old_col)

        result = move_player(board, current_player, next_row, next_col)

        if result == 'Busy Position':
            print("You can't stand on an occupied position!")
            continue

        if result:
            the_king_is_captured(
                board,
                current_player,
                next_row,
                next_col,
                old_row,
                old_col
            )
            break

        if current_player == 'W':
            board[white_row][white_col] = '_'
            white_row, white_col = next_row, next_col
        else:
            board[black_row][black_col] = '_'
            black_row, black_col = next_row, next_col

        current_player, second_player = second_player, current_player
        iteration += 1

        # Every fifth iteration the king change it's position.
        if iteration % 5 == 0:
            board[king_row][king_col] = '_'
            king_row, king_col = randint(0, SIZE - 1), randint(0, SIZE - 1)
            board[king_row][king_col] = 'K'
    else:
        print('GAME OVER! The King is Saved!')


if __name__ == "__main__":
    main()

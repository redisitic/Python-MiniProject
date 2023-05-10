board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
    ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
    [' ', '.', ' ', '.', ' ', '.', ' ', '.'],
    ['.', ' ', '.', ' ', '.', ' ', '.', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

def print_board(board):
    for row in board:
        print(" ".join(str(piece) for piece in row))

def get_move():
    move = input("Enter move (e.g. 'a2a4'): ")
    return (int(move[1]) - 1, ord(move[0]) - 97, int(move[3]) - 1, ord(move[2]) - 97)

def make_move(board, move):
    row1, col1, row2, col2 = move
    board[row2][col2] = board[row1][col1]
    board[row1][col1] = ' '
    return board

print_board(board)

while True:
    move = get_move()
    board = make_move(board, move)
    print_board(board)
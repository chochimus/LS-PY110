import random
import os

def display_board(board, score):
    os.system('clear')
    prompt(f"You are {X_MARKER}. Computer is {O_MARKER}.")
    prompt(f"Score: P - {score['Player']} C - {score['Computer']}")
    print('     |     |')
    print(f'  {board[0]}  |  {board[1]}  |  {board[2]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[3]}  |  {board[4]}  |  {board[5]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[6]}  |  {board[7]}  |  {board[8]}')
    print('     |     |')
    print('')

def prompt(message):
    print(f'==> {message}')

def empty_squares(board):
    return [i for i,num in enumerate(board) 
                     if num == EMPTY_MARKER]

def join_or(lst, delim=', ', last='or'):
    if not lst:
        return ''
    if len(lst) == 1:
        return str(lst[0])
    if len(lst) == 2:
        return f'{lst[0]} {last} {lst[1]}'
    
    leading_items = delim.join(str(item) for item in lst[0:-1])
    return f'{leading_items}{delim}{last} {lst[-1]}'


def player_chooses_square(board):
    
    while True:
        valid_choices = [str(num + 1) for num in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        try:
            square = int(input().strip())
        except ValueError:
            prompt("Sorry, that's not a valid choice.")
            continue
        if str(square) in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[square - 1] = X_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = None
    for line in WINNING_LINES:
        square = immediate_threat(line, board, O_MARKER)
        if square != None:
            break
    if square == None:
        for line in WINNING_LINES:
            square = immediate_threat(line, board, X_MARKER)
            if square != None:
                break
    
    if square == None:
        if 4 in empty_squares(board):
            square = 4
        else:    
            square = random.choice(empty_squares(board))

    board[square] = O_MARKER

def immediate_threat(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == EMPTY_MARKER:
                return square
    return None
        
def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    return bool(detect_winner(board))

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == X_MARKER
            and board[sq2] == X_MARKER
            and board[sq3] == X_MARKER):
            return 'Player'
        elif (board[sq1] == O_MARKER
                  and board[sq2] == O_MARKER
                  and board[sq3] == O_MARKER):
            return 'Computer'
    return None

EMPTY_MARKER = " "
X_MARKER = "X"
O_MARKER = "O"
GAMES_TO_WIN_MATCH = 5 
WINNING_LINES = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

def choose_square(board, current_player):
    if current_player == 'Player':
        player_chooses_square(board)
    else: 
        computer_chooses_square(board)
def alternate_player(current_player):
    if current_player == 'Player':
        return 'Computer'
    else:
        return 'Player'
def play_tic_tac_toe():
    score = {'Player': 0, 'Computer': 0}
    while True:
        board = [' '] * 9
        current_player = 'Player'
        while True:
            display_board(board, score)
            choose_square(board, current_player)
            current_player = alternate_player(current_player)
            if someone_won(board) or board_full(board):
                break

        display_board(board, score)

        if someone_won(board):
            winner = detect_winner(board)
            prompt(f'{winner} won!')
            score[winner] += 1
            if(score[winner] == GAMES_TO_WIN_MATCH):
                prompt(f'{winner} wins match!')
                score['Player'] = score['Computer'] = 0
        else:
            prompt("It's a tie!")

        while True:
            prompt("Play again? (y or n)")
            answer = input().strip().lower()

            if answer == 'y' or answer == 'n':
                break
            prompt("That's not a valid choice")
        if answer != 'y':
            break
    
    prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()
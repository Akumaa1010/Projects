board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
Player1 = "X"
winner = "None"
gamerunner = True


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def player_input(board):
    inp = int(input("Put a number between 1-9 : \n"))
    if 1 <= inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = Player1
    else:
        print("Invalid Number")
        player_input(board)


# Check Horizontal
def Check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


# Check Vertical
def Check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[2]
        return True


# Check Diagonal
def Check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True


def Check_win(board):
    global gamerunner
    if Check_diagonal(board):
        gamerunner = False
        print_board(board)
        print("Congrats!! Player " + winner + " wins!")
    elif Check_vertical(board):
        gamerunner = False
        print_board(board)
        print("Congrats!! Player " + winner + " wins!")
    elif Check_horizontal(board):
        print_board(board)
        print("Congrats!! Player " + winner + " wins!")
        gamerunner = False


def check_tie(board):
    global gamerunner
    if "-" not in board:
        print_board(board)
        gamerunner = False
        print("Tie!")
        return True


while (gamerunner):
    print_board(board)
    player_input(board)
    Check_win(board)
    if gamerunner:
        check_tie(board)
    if Player1 == "X":
        Player1 = "0"
    else:
        Player1 = "X"



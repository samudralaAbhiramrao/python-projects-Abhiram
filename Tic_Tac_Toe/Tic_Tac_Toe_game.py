# gloabl variable declaration
game_still_going = True
winner = None
current_player = "X"
# declaring board variable just to dsign the look of our play_game
# we consider on list bcz we can able to change easily
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# display_board() is used to just display the layout of the board intially


def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

# play_game() is where actuall game is controlled and organised and other fuctioins are called


def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        Flip_player()
    if winner == "X" or winner == "O":
        print(winner+""" won😎""")
    elif winner == None:
        print("""TIE 🤣☠""")
    return


def handle_turn(player):
    print(player + "'s Turn.'")
    position = input("chose a position from 1 to 9 :")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("INVALID CHOICE 😒choose between 1 to 9 :")
        position = int(position)-1
        if board[position] == "-":
            valid = True
        else:
            print("yo you cant do that 🤷‍♂️ its filled ")
    board[position] = player
    display_board()
    return


# checks whether the game is over or not
def check_if_game_over():
    # which contains two function where as to declare that who is won or is it a tie
    check_if_win()  # checks whether "X" or "O" won
    check_if_tie() 	# checks that when board is filled is it a tie or not
    return


# check whether which  player has won and if not is it a tie
def check_if_win():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagnol()

    # so here we have set the winner as a gloabl in this function to change its value ,bcz actualy winner variable is a gloabl variable and so to access it in a function we need to declare it as gloabl in the function
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None  # here when al the box is complete and its a tie then we set winner as none so when the play_game() starts executing it displays as TIE when it happened
    return


# checks in row
def check_row():
    # this variable is a global variable and checks the game is running or not
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_still_going = False

    # below statements return  who have won game  by returning " X "  or " O "
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

# checks in column


def check_column():
    # this variable is a global variable and checks the game is running or not
    global game_still_going
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        game_still_going = False

    # below statements return  who have won game  by returning " X "  or " O "
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


# checks diagonally
def check_diagnol():
    # this variable is a global variable and checks the game is running or not
    global game_still_going
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2:
        game_still_going = False

    # below statements return  who have won game  by returning " X "  or " O "
    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    return


# cheks if the game is TIE
def check_if_tie():
    global game_still_going
    # checks whether there is any empty space available or not in the board and if ther is no empty then the game will be stopped and the output will be a tie
    if "-" not in board:
        game_still_going = False
    return

# used to switch between players


def Flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()

# play_game()
# 		display_board()
# 		handle_turn() used to handle turns
# check_if_game_over()
# 		Check_win()
# 			Check_row()
# 			check_column()
# 			check_diagnol()
# 		Check_Tie()
# Flip_player()

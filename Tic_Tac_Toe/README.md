# TIC-TAC-TOE😎

> Basically this game sontains 2 players "X" and "O". and these players will be played on the comman board and based on there selected location they would be marked and ay last based on the order of matching 3 same symbols in order the player will be **WON**

## **Abstract of code**📒

> 1.  **global variable declaration🌎**
> 2.  **Board layout**
> 3.  **Functions**
>     1.  **display_board()**
>     2.  **play_game()**
>     3.  **handle_turn()**
>     4.  **check_if_game_over()**
>         1. **check_if_win()**
>            1. **check_row()**
>            2. **check_column()**
>            3. **check_diagonal()**
>         2. **check_if_tie()**
>     5.  **Flip_player()**

## CODE-Functionality🚀

### **Global Variables🌎**

```python
game_still_going = True
winner = None
current_player = "X"
```

### **Board basic Layout😪**

```python
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
```

### **Functions**🔥

## 1. **display_board()🤟**

> This function is used to display the board in a correct format.

```python
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

```

## 2. **play_game()🧠**

> This function is used to actually start the game .This code is breaked and explained in Parts see Below👇

#### Intial Step 🔴

> Initally the function is called and at first the display_board() is called and when it is called a plane board is displayed.

```python
def play_game():
    display_board()
```

### looping🌑🌒🌓🌔🌕🌖🌗🌘

> Here we conatin a While loop which is used to play the game until it ends and in this while loop we included 3 functions call's.

```python
while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        Flip_player()
```

### Print statements📺

> Here after the end of the game i.e: end of while loop we need to display who have Won or Tie . so we take a ifelse statement and print .

```python
if winner == "X" or winner == "O":
        print(winner+""" won😎""")
    elif winner == None:
        print("""TIE 🤣☠""")
    return
```

### Final code of Play_game()📌

```python
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
```

## 3. **Handle_Turn()⌛**

> This function is used to Handle the players turn and not allow the user to use the same location which is changed and also used to handle invalid inputs i.e: other than **"X"** or **"O"** .
> I have borke this function to explain in detail , see below to understand what is happening👇👀

### Inital Step🟠

> we simply take the input from the user and cast it to integer and assgin the value to boards prefered location.

```python
def handle_turn():
 position=input("choose a position from 1 to 9:")
 position = int(position) - 1
 board[position] = "X"

```

### Player Parameter👨👩

> we basically pass the player as a parameter to this function and helps to know who have assigned the value and also can be used to know who have won the game if there is no Tie.Here instead of assigning some value to the board we take the player name as a value

```python
def handle_turn(player):
 position=input("choose a position from 1 to 9:")
 position = int(position) - 1
 board[position] = player
 display_board()
```

### Handling Invalid Inputs

> So in this code we are handling the input field that is been given by the user i,e: whenever a wrong input or invalid input given by the user we display a message

> All these are done in a while loop which checks a condition from the mentioned list of numbers , if the input given is not in that list then the error message is printed and allowed the user to given input again and when the user gives the correct input the while loop will be stops its execution and the board is aggined with the "X" or "O" based on the player's turn

```python
def handle_turn(player):
 print(player + " 's Turn🎇.")
 position=input("choose a position from 1 to 9:")
 while position not in ["1","2","3","4","5","6","7","8","9"]:
  position = input("INVALID CHOICE 😒choose between 1 to 9 :")
 position = int(position) - 1
 board[position] = player
 display_board()
```

### Stoping Overriding the values

> Here in the function we take a variable "valid" and assign **False** to it initally , and a while loop is used which checks if the given valid is true or false and this while loop bounds all the other while loops ionto it and whe the applied condition is correct then the while loop is executed and in that way the overriding of the value is done

```python

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
```

### Final code of handle_turn(player)📌

```python
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
```

## 4. **check_if_game_over()⌚**

> This function is used to check the game is over or not and tell who have **won** or is it a **Tie**

> This function is divide as 2 parts namely

1.  check_if_win()
2.  check_if_tie()

These mentioned function functionality is mentioned in bottom check it out

```python
def check_if_game_over():
 check_if_win()
 check_if_tie()
```

## 4.1 **check_if_win()👑**

> This functioned is used to find who have won and checking in all the posiblities of winning is done.
> This is again subdivided further in 3parts for checking in row-wise ,column-wise and diagnol-wise matches.

> Based on the match the respective player name is returned and given to the print statement in the play_game()

```python
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
        winner = None
         # here when al the box is complete and its a tie then we set winner as none so when the play_game() starts executing it displays as TIE when it happened
    return
```

## 4.1.1 **check_rows()🥇**

> This functions checks in row-wise and gives the value to its parent function .Basically in this function rows are checked based on there position respective values and the player name is taken

```python
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
```

## 4.1.2 **check_columns()🥇**

> This functions checks in column-wise and gives the value to its parent function .Basically in this function columns are checked based on there position respective values and the player name is taken

```python
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
```

## 4.1.3 **check_diagonals()🥇**

> This functions checks in diagonal-wise and gives the value to its parent function .Basically in this function diagonals are checked based on there position respective values and the player name is taken

```python
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
```

## 4.2 **check_if_tie()🎀**

>checks if there are "-"in the board and if there is no "-" then the program stops else it continues its execution.

>If  "-" is not present in the board then it prints **TIE**

```python
def check_if_tie():
    global game_still_going
    # checks whether there is any empty space available or not in the board and if ther is no empty then the game will be stopped and the output will be a tie
    if "-" not in board:
        game_still_going = False
    return
```

## 5. **Flip_player()👨👩**

>This function flips between players 

```python
def Flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
```



# Finally🏳🏴🏳🏴🏳🏴🏳🏴🏳🏴🏳🏴

>Game is started with a function call as :

```python
play_game()
```
# Playing LOL!!!!😁
## Winning🥇
![WON](https://github.com/samudralaAbhiramrao/python-projects-Abhiram/blob/main/Tic_Tac_Toe/output_Images/won.png "Payer_won")

## Verifcation of conditions💡
![Verifications](https://github.com/samudralaAbhiramrao/python-projects-Abhiram/blob/main/Tic_Tac_Toe/output_Images/verifyingConditions.png "Verifying conditions")

## TIE🎀
![Tie](https://github.com/samudralaAbhiramrao/python-projects-Abhiram/blob/main/Tic_Tac_Toe/output_Images/TIE.png "Tie")

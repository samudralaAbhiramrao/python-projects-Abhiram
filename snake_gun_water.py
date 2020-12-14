import random


def game(computer, you):
    if computer == you:
        return None
    elif computer == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif computer == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif computer == "g":
        if you == "s":
            return False
        elif you == "w":
            return True


a = random.randint(1, 3)
if a == 1:
    computer = "s"
elif a == 2:
    computer = "w"
else:
    computer = "g"
print("computer turn snake(s) , Gun(g) , Water(w) ...... Its has selected now your turn")
you = input(" Snake(s) , Gun(g) , Water (w)")
b = game(computer, you)
print(f"computer selected {computer}")
if b == None:
    print("its a tie!")
elif(b):
    print("YOU WON!!")
else:
    print("you LOSE!!!")


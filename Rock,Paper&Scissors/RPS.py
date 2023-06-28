import random
def Game():

    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    you = int(input("Enter your choice (0 for rock, 1 for paper, 2 for scissors): "))
    print("Computer chose:", computer)

    if ((you == 0 and computer == "paper") or
        (you == 1 and computer == "scissors") or
        (you == 2 and computer == "rock")):
        if you == 0:
            print("You chose: rock")
        elif you == 1:
            print("You chose: paper")
        else:
            print("You chose: scissors")
        print("Computer won!")
    elif you == choices.index(computer):
        print("It's a draw!")
    else:
        print("You won!")

    play = ["yes","no"]
    playagain = input("Do you want to play again y for yes, n for no: ")
    if (playagain == "y"):
        Game()
    else:
        print("Thankyou for playing!")

Game()
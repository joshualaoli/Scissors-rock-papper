# rock, scissors, papper project

from getpass import getpass as input #to ensure that whenever you use input, each player cannot see what the other player typed in

print("r for Rock, s for Scissors, p for Paper")
print("")
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")

if player1 == "r":
    if player2 == "r":
        print("Both of you picked Rock - Draw! ")
    elif player2 == "s":
        print("Rock vs Scissors, rock win!!")
    elif player2 == "p":
        print("Rock vs Paper, paper win!")
elif player1 == "s":
    if player2 == "s":
        print("Both of you picked Scissors - Draw! ")
    elif player2 == "r":
        print("Rock vs Scissors, rock win!!")
    elif player2 == "p":
        print("Scissors vs Paper, scisors win!")
elif player1 == "p":
    if player2 == "p":
        print("Both of you picked Paper - Draw! ")
    elif player2 == "r":
        print("Rock vs Paper, rock win!!")
    elif player2 == "s":
        print("Scissors vs Paper, scissors win!")
else:
    print("Invalid typo")

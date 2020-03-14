import time
import random


def rockpaperscissors():
    options = ['ROCK', 'PAPER', 'SCISSORS']
    print("Rock!")
    time.sleep(0.5)
    print("Paper!")
    time.sleep(0.5)
    print("Scissors!")
    time.sleep(0.5)
    print("Shooooooot!!!")

    comp = random.choice(options)
    user = input("Your Choice: ").upper()

    if user not in options:
        return "Invalid input"

    if comp == user:
        return "Draw game!"
    elif comp == "ROCK" and user == "PAPER":
        return "You Win, "+user+" beats "+comp
    elif comp == "SCISSORS" and user == "ROCK":
        return "You Win, "+user+" beats "+comp
    elif comp == "PAPER" and user == "SCISSORS":
        return "You Win, "+user+" beats "+comp
    else:
        return "Computer Wins, "+comp+" beats "+user

for i in range(1,4):
  print(rockpaperscissors())
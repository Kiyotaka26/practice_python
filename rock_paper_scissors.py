'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out
a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

-Rock beats scissors

-Scissors beats paper

-Paper beats rock

'''
from secrets import choice

xd = ["rock", "paper", "scissors"]

print()
print("WELCOME TO THE ROCK, PAPER AND SCISSORS GAME")

print()

print("Remember:\n\n-Rock beats scissors\n-Scissors beats paper\n-Paper beats rock\n\nEnjoy :)")

print()

def rock():
    if choice(xd) == "rock":
        print(f"The result of this match was a draw, the computer have choosed rock too")
    elif choice(xd) == "paper":
        print(f"You have losed, the computer have choosed paper")
    else:
        print(f"You have winned, the computer have choosed scissors")
def paper():
    if choice(xd) == "paper":
        print(f"The result of this match was a draw, the computer have choosed paper too")
    elif choice(xd) == "scissors":
        print(f"You have losed, the computer have choosed scissors")
    else:
        print(f"You have winned, the computer have choosed rock")
def scissors():
    if choice(xd) == "scissors":
        print(f"The result of this match was a draw, the computer have choosed scissors too")
    elif choice(xd) == "rock":
        print(f"You have losed, the computer have choosed rock")
    else:
        print(f"You have winned, the computer have choosed paper")


def mmm():
    print()
    while True:
        question = input("Do you want to play again? ")
        if question.lower() == "yes":
            run()
        elif question.lower() == "no":
            break
        else:
            print("Do you have to choose yes or no")


def run():
    print()
    while True:
        election = input("Choose rock, paper or scissors: ")
        if election.lower() == "rock":
            print()
            rock()
            mmm()
            break
        elif election.lower() == "paper":
            print()
            paper()
            mmm()
            break
        elif election.lower() == "scissors":
            print()
            scissors()
            mmm()
            break
        else:
            print()
            print("You have to choose rock, paper, or scissors")
            mmm()
            break


if __name__ == '__main__':
    run()
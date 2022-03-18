'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 


Extras:

1-Keep the game going until the user types “exit”.

2-Keep track of how many guesses the user has taken, and when the game ends, print this out.

'''
import random

def counter():
    counter.number += 1
    return counter.number
counter.number = 0


def run():
    try:
        print()
        numero_aleatorio = random.randint(1, 9)
        numero_elegido = int(input("Choose a number between 1 and 9: "))


        while numero_elegido != numero_aleatorio:

            if numero_elegido < numero_aleatorio:
                
                print()
                print("Search for a larger number")

            else:
                print()
                print("Search for a lower number")


            print()
            numero_elegido = int(input("Choose another number: "))


            for i in range(1):
                print(counter())


        print()


        print("You have winned!")
        print(f"You have tried {counter() - 1} times until the victory")

    except ValueError:
        print()
        print("Goodbye")




































# def run():
#     print(random_number)
#     selection = int(input("Choose a number between 1 and 9: "))

#     while selection != random_number:
#         if selection > random_number:
#             print("Too high")
#         elif selection < random_number:
#             print("Too low")
#         else:
#             print("You have to choose a number between 1 and 9.")
#         question = input("Do you want to try again? ")
#         if question == "yes":
#             selection = int(input("Try again: "))
#         elif question == "exit":
#             break
#         else:
#             print("You have to choose yes or exit.")
#             run()
#     print("Congratulations! You got it right")











if __name__ == '__main__':
    run()









































# xd = choice(number)
# print(xd)
# print()

# def program():
#     selection = int(input("Choose a number between 1 and 9: "))
#     if selection == xd:
#         print("Congratulations! You got it right")
#     else:
#         if selection > xd:
#             print("Too high")
#         else:
#             print("Too low")







# while True:
#     program()
#     question = input("Do you want to try again? ")
#     if question.lower() == "yes":
#         program()
#     elif question.lower() == "exit":
#         break
#     else:
#         election = input("You have to choose yes or exit: ")
#         if election == "yes":
#             principal()
#         elif election == "exit":
#             break
#         else:
#             print(election)



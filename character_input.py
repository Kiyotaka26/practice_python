'''Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year 
(and therefore be out of date the next year).


Extras:

1-Add on to the previous program by asking the user for another number and printing out that many copies of the 
previous message.

2-Print out that many copies of the previous message on separate lines. 

'''

from datetime import datetime
from datetime import timedelta
from datetime import date

now = date.today()
print()
name = input("What is your name: ")
print()
birth = input("When you where born? write the date like this example YYYY-MM-DD: ")

def run():
    z = date.fromisoformat(birth)
    a = date.fromisoformat(str(now))

    born = a - z
    borned = born.days // 365
    total = z.year + 100
    
    if borned > 100:
        print()
        print("You are not a clown, you're the entire circus")
    else:
        print()

        print(f'Hello {name}.\nNow you have {borned} years old, which means that you will have 100 years old in {total}.')    

        print()

        character = int(input("How many times do you want to print the previous message? "))

        print()

        for i in range(character):
            print(f'Hello {name}.\nNow you have {borned} years old, which means that you will have 100 years old in {total}.\n') 


if __name__ == '__main__':
    run()
'''Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
to the user. Hint: how does an even / odd number react differently when divided by 2?


Extras:

1-If the number is a multiple of 4, print out a different message.

2-Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check 
divides evenly into num, tell that to the user. If not, print a different appropriate message.

'''
print()
number = float(input("Choose a number, to know if it is odd or even: "))


def run():
    
    print()
    if number % 4 == 0:
        print("This number is an even and a multiple of 4")

    elif number % 2 == 0:
        print("This is an even number")

    else:
        print("This is an odd number")

    print()
    divide = int(input("Choose a number to divide: "))
    print()
    divide_by = int(input("Choose a number to divide the previous number: "))
    division = (divide % divide_by) 

    print()
    if division == 0:
        print("The result between the division is an even number")
    else:
        print("The result between the division is an odd number")

if __name__ == '__main__':
    run()
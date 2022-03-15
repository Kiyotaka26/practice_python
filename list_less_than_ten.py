'''Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

1-Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list
in it and print out this new list.

2-Write this in one line of Python.

3-Ask the user for a number and return a list that contains only elements from the original list a that are smaller
than that number given by the user.

'''
import time


print()

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(f'The list is --> {a}')

print()
time.sleep(1)

less_than_5 = [elements for elements in a if elements < 5]  # <--This are the numbers that are less than 5
print(f'These are the numbers of the list that are less than 5 -- > {less_than_5}')

print()
time.sleep(1)

def run():
    number = float(input("Type the limit number of the list, and the console will print the numbers of the list that are less than the given number: "))

    print()
    time.sleep(1)

    less_than_number = [elements for elements in a if elements < number]
    print(f'These are the numbers of the list that are less than {round(number)} -- > {less_than_number}')


if __name__ == '__main__':
    run()

'''Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common 
between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1-Randomly generate two lists to test this.

2-Write this in one line of Python (don't worry if you can't figure this out at this point - we'll get to it soon)

'''
print()
import random

list_1 = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
list_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

print("These are the two lists: ")
print()
print(list(list_1))
print(list(list_2))

my_list = list_1 | list_2
print()
print(f'These are the numbers that are common in the two lists --> {list(my_list)}')

print()

# Extras:

selection = int(input("How many numbers do you want to see in the two random list: "))

l = list(range(1, selection + 1))

print()

lr_1 = random.sample(l, len(l))
print(f'First random list --> {lr_1}')

print()

lr_2 = random.sample(l, len(l))
print(f'Second random list --> {lr_2}')

print()

lr_3 = set(lr_1) | set(lr_2)
print(f'These are the numbers that are common in the two lists --> {list(lr_3)}')
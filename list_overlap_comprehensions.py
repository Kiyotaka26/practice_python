'''Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extra:

Randomly generate two lists to test this

'''
import random


def union(n):
    def numbers(x):
        return x | n
    return numbers



list_1 = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
list_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}


un = union(list_1)
un2 = un(list_2)


print()
print(list(un2))


print()

question = int(input("How many numbers do you want to print on the random list: "))

print()

randomlist = random.sample(range(1, 100), question)
randomlist_1 = random.sample(range(1, 100), question)

un = union(set(randomlist))
un2 = un(set(randomlist_1))
xd = sorted(list(un2))
print(xd)

'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.'''

import random

a = [5, 10, 15, 20, 25]
print(f'The first list is --> {a}')

randomlist = random.sample(range(10, 30), 5)

def union(n):
    def numbers(x):
        return [n, x]
    return numbers

def run():
    first_element = a[0]
    second_element = a[-1]

    element_1 = randomlist[0]
    element_2 = randomlist[-1]

    un = union(first_element)
    un2 = un(second_element)
    print(un2)

    print()

    print(f'The second list, which is random is --> {randomlist}')
    un = union(element_1)
    un2 = un(element_2)
    print(un2)
    
if __name__ == '__main__':
    run()
'''
Let's say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
'''
print()

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(f'Original list --> {a}')

print()

list_comprehension = [i for i in a if i % 2 == 0]
print(f'The even numbers of the previous list are --> {list_comprehension}')
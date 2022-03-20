'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.'''

print()

a = int(input('Give amount: '))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a    # This iterates the elements you put in "a". For example, if there are 12, this iterates all 12 items in the list.
        a, b = b, a + b      # (3, 5 = 3, 5 + 3) == (5, 8 = 5, 8 + 5) == (8, 13 = 8, 13 + 8)...

print()

print(list(fib(a)))
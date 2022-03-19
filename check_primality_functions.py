'''Ask the user for a number and determine whether the number is prime or not.'''
print()
number = int(input("Choose a number to know if it is prime: "))

prime = [i for i in range(1, number + 1) if number % i == 0]

print()

if prime == [1, number]:
    print("Is prime")
else:
    print("Is not prime")



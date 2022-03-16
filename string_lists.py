'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)

'''

print()

question = input("Write something to know if it is a palindrome: ")

print()

if question.lower() == question.lower()[::-1]:
    print("It is a palindrome")
else:
    print("It isn't a palindrome")
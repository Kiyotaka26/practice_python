'''Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password. 

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.'''


import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

question = input("Do you want a weak random password or a strong random password? ")



def options():
    if question == "weak":
        password = ''.join(random.choice(characters) for i in range(2))
    else:
        password = ''.join(random.choice(characters) for i in range(8))


    print(password)



if __name__ == '__main__':
    options()
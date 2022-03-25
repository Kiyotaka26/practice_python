'''Write a program (using functions!) that asks the user for a long string containing multiple words.

 Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  "My name is Michele"

  Then I would see the string:

  "Michele is name My"

  shown back to me.'''

question = input("Write a quote to see it backwards: ")

def run():   
    words = question.split()
    words = list(reversed(words))
    print(" ".join(words))

if __name__ == '__main__':
    run()
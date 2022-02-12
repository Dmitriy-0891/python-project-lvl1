#!:/usr/bin/env python3

import prompt
import random

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    x = 1
    while x <= 4:
        if x == 4:
            print("Congratulations, " + name + "!")
        else:
            count = random.randint(1,999999)
            print("Questin: " + str(count))
            answer = prompt.string('Your answer: ')
            if count % 2 == 0:
                if answer == 'yes':
                    print("Correct!")
                else:
                    print( "'" + answer + "' is wrong answer:(. Correct answer is 'yes'.\nLet`s try again " + name + "!")
                    break
            else:
                if answer == 'no':
                    print("Correct!")
                else:
                    print( "'" + answer + "' is wrong answer:(. Correct answer is 'no'.\nLet`s try again " + name + "!")
                    break
        x += 1
        
        
            


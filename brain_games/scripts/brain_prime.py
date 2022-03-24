#!:/usr/bin/env python3

import prompt
import random


def main():
    x = 0
    while x >= 0:
        print('Welcome to the Brain Games!')
        name = prompt.string('May I have your name? ')
        print('Hello, ' + name + '!')
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        num = random.randint(0, 3752)
        print('Question: ' + str(num))
        answer = prompt.string('Your answer: ')
        d = 2
        while num % d != 0:
            d += 1
        if num == d:
            if answer == "yes":
                print("Correct!")
            else:
                print("'" + answer + "' is wrong answer:(. Correct answer is 'yes'.")
                print("Let`s try again " + name + "!")
        else:
            if answer == "no":
                print("Correct!")
            else:
                print("'" + answer + "' is wrong answer:(. Correct answer is 'no'.")
                print("Let`s try again " + name + "!")
        
        x += 1


if __name__ == '__main__':
    main()
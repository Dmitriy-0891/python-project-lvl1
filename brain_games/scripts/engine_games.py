#!:usr/bin/env python3

import prompt
import random
from brain_games import brain_calc

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is result of the exrpession?')
    x = 1
        while x <= 4:
        if x == 4:
            print("Congratulations, " + name + "!")
        else:
            brain_calc()

        x += 1


if __name__ == '__main__':
    main()


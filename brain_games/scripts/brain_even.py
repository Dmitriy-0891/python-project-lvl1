#!:/usr/bin/env python3

import prompt
import random


def main():
    count = random.randint(1, 999999)
    print("Questin: " + str(count))
    answer = prompt.string('Your answer: ')
    if count % 2 == 0:
        if answer == 'yes':
            print("Correct!")
        else:
            print("'" + answer + "' is wrong answer:(. Correct answer is 'yes'")
            print("Let`s try again " + name + "!")
            break
    
    else:
        if answer == 'no':
            print("Correct!")
        else:
            print( "'" + answer + "' is wrong answer:(. Correct answer is 'no'")
            print("Let`s try again " + name + "!")
            break


if __name__ == '__main__':
    main()

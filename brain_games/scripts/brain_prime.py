#!:/usr/bin/env python3

import prompt
import random


def main():
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
            break
    else:
        if answer == "no":
            print("Correct!")
        else:
            print("'" + answer + "' is wrong answer:(. Correct answer is 'no'.")
            print("Let`s try again " + name + "!")
            break


if __name__ == '__main__':
    main()

#!:/usr/bin/env python3

import prompt
import random


def main(name, attempt_number):
    num = random.randint(0, 3752)
    print(f"Question: {num}")
    answer = prompt.string('Your answer: ')
    d = 2
    while num % d != 0:
        d += 1
    if num == d:
        if answer == "yes":
            print("Correct!")
            return True
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is 'yes'.")
            print("Let`s try again " + name + "!")
            return False
    else:
        if answer == "no":
            print("Correct!")
            return True
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is 'no'.")
            print("Let`s try again " + name + "!")
            return False


if __name__ == '__main__':
    main()

#!:/usr/bin/env python3

import prompt
import random


def main():
    num = random.randint(0, 3752)
    print(f"Question: {num}")
    answer = prompt.string('Your answer: ')
    d = 2
    while num % d != 0:
        d += 1
    if num == d:
        if answer == "yes":
            return True
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is 'yes'.")
            return False
    else:
        if answer == "no":
            return True
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is 'no'.")
            return False


if __name__ == '__main__':
    main()

#!:/usr/bin/env python3

import prompt
import random


def prime(num):
    d = 2
    while num % d != 0:
        d += 1
    if num == d:
        result = "yes"
    else:
        result = "no"
    return result


def main(x=1):
    general_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    num = random.randint(0, 3752)
    question = f"Question: {num}"
    result = prime(num)
    return (question, result, general_question)


if __name__ == '__main__':
    main()

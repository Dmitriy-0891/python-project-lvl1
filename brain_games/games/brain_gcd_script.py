#!:/usr/bin/env python3

import prompt
import random


def gcd(num_1, num_2):
    pgcd = 1
    gcd = 1
    if num_1 > num_2:
        # possible greatest common divisor
        pgcd = num_2
    else:
        pgcd = num_1

    for i in range(pgcd, 1, -1):
        if num_1 % i == 0:
            if num_2 % i == 0:
                # greatest common divisor
                gcd = i
                break
    return gcd


def main(x=1):
    general_question = "Find the greatest common divisor of given numbers."
    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    question = f"Question: {num_1} {num_2}"
    result = gcd(num_1, num_2)
    return (question, result, general_question)


if __name__ == '__main__':
    main()

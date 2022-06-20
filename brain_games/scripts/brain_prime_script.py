#!:/usr/bin/env python3

import prompt
import random


def main(x=1):
    num = random.randint(0, 3752)
    print(f"Question: {num}")
    answer = prompt.string('Your answer: ')
    d = 2
    while num % d != 0:
        d += 1
    if num == d:
        result = "yes"
    else:
        result = "no"
    return [answer, result]


if __name__ == '__main__':
    main()

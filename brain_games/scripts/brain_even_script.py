#!:/usr/bin/env python3

import prompt
import random


def main(x=1):
    count = random.randint(1, 999999)
    print("Question: " + str(count))
    answer = prompt.string('Your answer: ')
    if count % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return [answer, result]


if __name__ == '__main__':
    main()

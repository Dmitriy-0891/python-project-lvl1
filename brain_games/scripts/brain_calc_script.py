#!:/usr/bin/env python3

import prompt
import random


def main(x=1):
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    list_arithmetic = ['+', '-', '*']
    sign = random.choice(list_arithmetic)
    print(f"Question: {num_1} {sign} {num_2}")
    answer = prompt.string('Your answer: ')
    if sign == "+":
        result = num_1 + num_2
    elif sign == "-":
        result = num_1 - num_2
    elif sign == "*":
        result = num_1 * num_2
    return [int(answer), result]


if __name__ == '__main__':
    main()

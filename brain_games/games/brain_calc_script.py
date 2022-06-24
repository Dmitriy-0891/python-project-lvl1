#!:/usr/bin/env python3

import random


def main(x=1):
    general_question = "What is result of the exrpession?"
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    list_arithmetic = ['+', '-', '*']
    sign = random.choice(list_arithmetic)
    question = f"Question: {num_1} {sign} {num_2}"
    if sign == "+":
        result = num_1 + num_2
    elif sign == "-":
        result = num_1 - num_2
    elif sign == "*":
        result = num_1 * num_2
    return (question, result, general_question)


if __name__ == '__main__':
    main()

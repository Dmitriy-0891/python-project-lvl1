#!:/usr/bin/env python3

import prompt
import random


def main(x=1):
    general_question = 'Answer "yes" if the number is even, otherwise answer "no"'
    count = random.randint(1, 999999)
    question = f"Question: {count}"
    if count % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return (question, result, general_question)


if __name__ == '__main__':
    main()

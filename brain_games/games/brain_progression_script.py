#!:/usr/bin/env python3

import random


def main(x=1):
    general_question = 'What number is missing in the progression?'
    num_first = random.randint(1, 1000000)
    step = random.randint(1, 1000)
    i = random.randint(0, 9)
    f = ".."
    last_number = num_first + (step * 10)
    progression = list(range(num_first, last_number, step))
    result = progression[i]
    del progression[i]
    progression.insert(i, f)
    question = "Question: "
    for k in progression:
        question = question + str(k) + " "
    return (question, result, general_question)


if __name__ == '__main__':
    main()

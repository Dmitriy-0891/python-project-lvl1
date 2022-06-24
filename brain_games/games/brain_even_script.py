#!:/usr/bin/env python3


import random


def main(x=1):
    gen_ques = 'Answer "yes" if the number is even, otherwise answer "no"'
    count = random.randint(1, 999999)
    question = f"Question: {count}"
    if count % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return (question, result, gen_ques)


if __name__ == '__main__':
    main()

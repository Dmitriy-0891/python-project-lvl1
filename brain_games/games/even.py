import random


RULE_GAME = 'Answer "yes" if the number is even, otherwise answer "no"'


def main():
    count = random.randint(1, 999999)
    question = f"Question: {count}"
    if count % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return (question, result)

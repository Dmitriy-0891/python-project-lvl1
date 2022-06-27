import random


RULE_GAME = "What is result of the exrpession?"


def main():
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
    return (question, str(result))

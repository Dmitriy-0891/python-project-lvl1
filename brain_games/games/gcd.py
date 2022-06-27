import random


RULE_GAME = "Find the greatest common divisor of given numbers."


def gcd(num_1, num_2):
    pgcd = min(num_1, num_2)
    gcd = 1
    for i in range(pgcd, 1, -1):
        if num_1 % i == 0:
            if num_2 % i == 0:
                # greatest common divisor
                gcd = i
                break
    return gcd


def main():
    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    question = f"Question: {num_1} {num_2}"
    return (question, str(gcd(num_1, num_2)))

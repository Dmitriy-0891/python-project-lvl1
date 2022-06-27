import random


RULE_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num == 0:
        return False
    elif num == 1:
        return False
    else:
        d = 2
        while num % d != 0:
            d += 1
        if num == d:
            return True
        else:
            return False


def main():
    num = random.randint(0, 3752)
    question = f"Question: {num}"
    if is_prime(num):
        result = "yes"
    else:
        result = "no"
    return (question, result)

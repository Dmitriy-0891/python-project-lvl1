import random


RULE_GAME = 'What number is missing in the progression?'


def main():
    num_first = random.randint(1, 1000000)
    step = random.randint(1, 1000)
    i = random.randint(0, 9)
    f = ".."
    last_number = num_first + (step * 10)
    progression = list(range(num_first, last_number, step))
    progression = [str(i) for i in progression]
    result = progression[i]
    progression[i] = f
    str_progression = " ".join(progression)
    question = f"Question: {str_progression}"
    return (question, str(result))

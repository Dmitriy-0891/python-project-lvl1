#!:/usr/bin/env python3

import prompt
import random


def main(name, attempt_number):
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    list_arithmetic = ['+', '-', '*']
    sign = random.choice(list_arithmetic)
    print(f"Question: {num_1} {sign} {num_2}")
    answer = prompt.string('Your answer: ')
    if sign == "+":
        result = num_1 + num_2
        if answer == str(result):
            print("Correct!")
            return True
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is {result}.")
            print("Let`s try again " + name + "!")
            return False
    
    elif sign == "-":
        result = num_1 - num_2
        if answer == str(result):
            print("Correct!")
            return True
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is {result}.")
            print("Let`s try again " + name + "!")
            return False

    elif sign == "*":
        result = num_1 * num_2
        if answer == str(result):
            print("Correct!")
            return True
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is {result}.")
            print("Let`s try again " + name + "!")
            return False


if __name__ == '__main__':
    main()

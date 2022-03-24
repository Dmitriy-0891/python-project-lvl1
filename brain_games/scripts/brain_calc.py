#!:/usr/bin/env python3

import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is result of the exrpession?')
    x = 1
    while x <= 4:
        if x == 4:
            print("Congratulations, " + name + "!")
        else:
            num_1 = random.randint(1, 99)
            num_2 = random.randint(1, 99)
            list_arithmetic = ['+', '-', '*']
            sign = random.choice(list_arithmetic)
            print("Question: " + str(num_1) + " " + str(sign) + " " + str(num_2))
            answer = prompt.string('Your answer: ')
            if sign == "+":
                result = num_1 + num_2
                if answer == str(result):
                    print("Correct!")
                else:
                    print("'" + answer + "' is wrong answer:(. Correct answer is " + str(result) + ".")
                    print("Let`s try again " + name + "!")
                    break
            elif sign == "-":
                result = num_1 - num_2
                if answer == str(result):
                    print("Correct!")
                else:
                    print("'" + answer + "' is wrong answer:(. Correct answer is " + str(result) + ".")
                    print("Let`s try again " + name + "!")
                    break
            elif sign == "*":
                result = num_1 * num_2
                if answer == str(result):
                    print("Correct!")
                else:
                    print("'" + answer + "' is wrong answer:(. Correct answer is " + str(result) + ".")
                    print("Let`s try again " + name + "!")
                    break


        x += 1


if __name__ == '__main__':
    main()

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
            first_count = random.randint(1,99)
            second_count = random.randint(1, 99)
            list_arithmetic = ['+', '-', '*']
            arifm_operator = random.choice(list_arithmetic)
            print("Question: " + str(first_count) + " " + str(arifm_operator) + " " + str(second_count))
            answer = prompt.string('Your answer: ')
            if arifm_operator == "+":
                result = first_count + second_count
                if answer == str(result):
                    print("Correct!")
                else:
                    print( "'" + answer + "' is wrong answer:(. Correct answer is " + str(result) + ".\nLet`s try again " + name + "!")
                    break
            elif arifm_operator == "-":
                result = first_count - second_count
                if answer == str(result):
                    print("Correct!")
                else:
                    print( "'" + answer + "' is wrong answer:(. Correct answer is " + str(result) + ".\nLet`s try again " + name + "!")
                    break
            elif arifm_operator == "*":
                result = first_count * second_count
                if answer == str(result):
                    print("Correct!")
                else:
                    print( "'" + answer + "' is wrong answer:(. Correct answer is " + str(result) + ".\nLet`s try again " + name + "!")
                    break
        x += 1

if __name__ == '__main__':
    main()
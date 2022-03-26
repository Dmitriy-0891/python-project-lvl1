#!:/usr/bin/env python3

import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    x = 1
    while x <= 4:
        if x == 4:
            print("Congratulations, " + name + "!")
        else:
            num_first = random.randint(1, 1000000)
            step = random.randint(1, 1000)
            i = random.randint(0, 9)
            f = ".."
            last_number = num_first + (step * 10)
            progression = list(range(num_first, last_number, step))
            right_answer = progression[i]
            del progression[i]
            progression.insert(i, f)
            num_1 = progression[0]
            num_2 = progression[1]
            num_3 = progression[2]
            num_4 = progression[3]
            num_5 = progression[4]
            num_6 = progression[5]
            num_7 = progression[6]
            num_8 = progression[7]
            num_9 = progression[8]
            num_10 = progression[9]
            print("Question: " + str(num_1) + " " + str(num_2) + " " + str(num_3) + " " + str(num_4) + " " + str(num_5) + " " + str(num_6) + " " + str(num_7) + " " + str(num_8) + " " + str(num_9) + " " + str(num_10))
            answer = prompt.string('Your answer: ')
            if answer == str(right_answer):
                print("Correct!")
            else:
                print("'" + answer + "' is wrong answer:(. Correct answer is " + str(right_answer) + ".\nLet`s try again " + name + "!")
                break
        x += 1


if __name__ == '__main__':
    main()

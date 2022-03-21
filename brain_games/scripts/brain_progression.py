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
            first_number = random.randint(1,1000000)
            step = random.randint(1,1000)
            i = random.randint(0,9)
            f = ".."
            last_number = first_number + (step * 10)
            progression = list(range(first_number, last_number, step))
            right_answer = progression[i]
            del progression[i]
            progression.insert(i,f)
            num_one = progression[0]
            num_two = progression[1]
            num_three = progression[2]
            num_four = progression[3]
            num_five = progression[4]
            num_six = progression[5]
            num_seven = progression[6]
            num_eight = progression[7]
            num_nine = progression[8]
            num_ten = progression[9]
            print("Question: " + str(num_one) + " " + str(num_two) + " " + str(num_three) + " " + str(num_four) + " " + str(num_five) + " " + str(num_six) + " " + str(num_seven) + " " + str(num_eight) + " " + str(num_nine) + " " + str(num_ten))
            answer = prompt.string('Your answer: ')
            if answer == str(right_answer):
                print("Correct!")
            else:
                print( "'" + answer + "' is wrong answer:(. Correct answer is " + str(right_answer) + ".\nLet`s try again " + name + "!")
                break
        x += 1

if __name__ == '__main__':
    main()
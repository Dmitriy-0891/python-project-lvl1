#!:/usr/bin/env python3

import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    x = 1
    while x <= 4:
        if x == 4:
            print("Congratulations, " + name + "!")
        else:
            num_1 = random.randint(1, 1000)
            num_2 = random.randint(1, 1000)
            print("Question: " + str(num_1) + " " + str(num_2))
            a = prompt.string('Your answer: ')
            pgcd = 1
            if num_1 > num_2:
                # possible greatest common divisor
                pgcd = num_2
            else:
                pgcd = num_1
            gcd = 1
            for i in range(pgcd, 1, -1):
                if((num_1 % i == 0) and (num_2 % i == 0)):
                    # greatest common divisor
                    gcd = i
            if a == str(gcd):
                print("Correct!")
            else:
                print("'" + a + "' is wrong answer:(. Correct answer is " + str(gcd) + ".")
                print("Let`s try again " + name + "!")
                break
        
        x += 1


if __name__ == '__main__':
    main()

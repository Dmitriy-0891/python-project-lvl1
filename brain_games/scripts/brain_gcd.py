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
            first_count = random.randint(1,1000)
            second_count = random.randint(1, 1000)
            print("Question: " + str(first_count) + " " + str(second_count))
            answer = prompt.string('Your answer: ')
            pgcd = 1
            if first_count > second_count:
                #possible greatest common divisor
                pgcd = second_count
            else:
                pgcd = first_count
            gcd = 1
            for i in range(pgcd, 1, -1):
                if((first_count % i == 0) and (second_count % i == 0)):
                    #greatest common divisor
                    gcd = i
            if answer == str(gcd):
                print("Correct!")
            else:
                print( "'" + answer + "' is wrong answer:(. Correct answer is " + str(gcd) + ".\nLet`s try again " + name + "!")
                break
        x += 1

if __name__ == '__main__':
    main()
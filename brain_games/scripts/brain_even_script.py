#!:/usr/bin/env python3

import prompt
import random


def main():
    count = random.randint(1, 999999)
    print("Question: " + str(count))
    answer = prompt.string('Your answer: ')
    if count % 2 == 0:
        if answer == 'yes':
            return True
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is 'yes'")
            return False

    else:
        if answer == 'no':
            print("Correct!")
            return True
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is 'no'")
            return False


if __name__ == '__main__':
    main()

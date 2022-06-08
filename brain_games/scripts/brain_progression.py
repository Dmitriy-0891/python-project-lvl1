#!:/usr/bin/env python3

import prompt
import random


def main():
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
    first_five_num = f"{num_1} {num_2} {num_3} {num_4} {num_5}"
    second_five_num = f"{num_6} {num_7} {num_8} {num_9} {num_10}"
    print(f"Question: {first_five_num} {second_five_num}")
    answer = prompt.string('Your answer: ')
    if answer == str(right_answer):
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer:(.")
        print(f"Correct answer is '{right_answer}'.")
        print(f"Let`s try again {name}!")
        break


if __name__ == '__main__':
    main()

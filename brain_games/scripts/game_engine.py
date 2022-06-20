#!:/usr/bin/env python3

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def main(name_game_module, name):
    for x in list(range(1, 5)):
        if x == 4:
            print(f"Congratulations, {name}!")
        else:
            result = name_game_module.main(x)
            a = result[0]
            b = result[1]
            if a == b:
                print("Correct!")
            else:
                print(f"'{a}' is wrong answer:(. Correct answer is '{b}'.")
                print(f"Let's try again, {name}!")
                break


if __name__ == '__main__':
    main()

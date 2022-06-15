import prompt
from brain_games.scripts import brain_gcd


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    for x in list(range(1, 5)):
        if x == 4:
            print("Congratulations, " + name + "!")
        else:
            if brain_gcd.main() is True:
                print("Correct!")
            else:
                print("Let`s try again " + name + "!")
                break


if __name__ == '__main__':
    main()

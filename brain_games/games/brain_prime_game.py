import prompt
from brain_games.scripts import brain_prime


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for x in list(range(1, 5)):
        if x == 4:
            print("Congratulations, " + name + "!")
        else:
            if brain_prime.main(name, x) is False:
                break


if __name__ == '__main__':
    main()

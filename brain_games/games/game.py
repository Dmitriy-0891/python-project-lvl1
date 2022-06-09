#!:/usr/bin/env python3

import random
import prompt
from brain_games.scripts import engine_games


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('We have 5 games:')
    print('brain_calc\n brain_even\n brain_gcd\n brain_prime\n brain_progression')
    game = prompt.string("What game do you want to play? ")

    if game == "brain_calc":
        print('What is result of the exrpession?')
        return engine_games.main(name, game)

    elif game == "brain_even":
        print('Answer "yes" if the number is even, otherwise answer "no".')
        return engine_games.main(name, game)

    elif game == "brain_gcd":
        print('Find the greatest common divisor of given numbers.')
        return engine_games.main(name, game)

    elif game == "brain_prime":
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        return engine_games.main(name, game)

    elif game == "brain_progression":
        print('What number is missing in the progression?')
        return engine_games.main(name, game)

    else:
        return print("Sorry, but there is no such game!")



#!:/usr/bin/env python3

from brain_games import brain_games
from brain_games.sripts import engine_games
from brain_games.scripts import brain_calc
from brain_games.sripts import brain_even
from brain_games.scripts import brain_gcd
from brain_games.scripts import brain_prime
from brain_games.scripts import brain_progesssion

def main():
    brain_games.main()
    print('We have 5 games:')
    print('brain_calc\n brain_even\n brain_gcd\n brain_prime\n brain_progression')
    game = prompt.string("What game do you want to play? ")

    if game == "brain_calc":
        print('What is result of the exrpession?')
        return engine_games.main(brain_calc.main())

    elif game == "brain_even":
        print('Answer "yes" if the number is even, otherwise answer "no".')
        return engine_games.main(brain_even.main())

    elif game == "brain_gcd":
        print('Find the greatest common divisor of given numbers.')
        return engine_games.main(brain_gcd.main())

    elif game == "brain_prime":
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        return engine_games.main(brain_prime.main())

    elif game == "brain_progression":
        print('What number is missing in the progression?')
        return engine_games.main(brain_progression.main())

    else:
        return print("Sorry, but there is no such game!")



#!:usr/bin/env python3

from brain_games.scripts import brain_calc
from brain_games.scripts import brain_even
from brain_games.scripts import brain_gcd
from brain_games.scripts import brain_prime
from brain_games.scripts import brain_progression


def main(name, game_script):
    x = 1
    while x <= 4:
        if x == 4:
            print("Congratulations, " + name + "!")
        else:
            if game_script == "brain_calc":
                if brain_calc.main(name, x) is False:
                    break

            elif game_script == "brain_even":
                if brain_even.main(name, x) is False:
                    break

            elif game_script == "brain_gcd":
                if brain_gcd.main(name, x) is False:
                    break

            elif game_script == "brain_prime":
                if brain_prime.main(name, x) is False:
                    break

            elif game_script == "brain_progression":
                if brain_progression.main(name, x) is False:
                    break
        x += 1


if __name__ == '__main__':
    main()

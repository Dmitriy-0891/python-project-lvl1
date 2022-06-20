from brain_games.scripts import brain_prime_script
from brain_games.scripts import game_engine


def main():
    name = game_engine.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_engine.main(brain_prime_script, name)


if __name__ == '__main__':
    main()

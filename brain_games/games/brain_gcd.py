from brain_games.scripts import brain_gcd_script
from brain_games.scripts import game_engine


def main():
    name = game_engine.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game_engine.main(brain_gcd_script, name)


if __name__ == '__main__':
    main()

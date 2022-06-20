from brain_games.scripts import brain_even_script
from brain_games.scripts import game_engine


def main():
    name = game_engine.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_engine.main(brain_even_script, name)


if __name__ == '__main__':
    main()

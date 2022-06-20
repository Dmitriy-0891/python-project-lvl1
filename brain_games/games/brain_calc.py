from brain_games.scripts import brain_calc_script
from brain_games.scripts import game_engine


def main():
    name = game_engine.welcome_user()
    print('What is result of the exrpession?')
    game_engine.main(brain_calc_script, name)


if __name__ == '__main__':
    main()

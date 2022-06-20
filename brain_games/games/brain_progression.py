from brain_games.scripts import brain_progression_script
from brain_games.scripts import game_engine


def main():
    name = game_engine.welcome_user()
    print('What number is missing in the progression?')
    game_engine.main(brain_progression_script, name)


if __name__ == '__main__':
    main()

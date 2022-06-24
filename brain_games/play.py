import prompt


def main(name_game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(name_game_module.main()[2])
    ROUNDS_COUNTS = 3
    for _ in range(ROUNDS_COUNTS):
        result = name_game_module.main(_)
        # a - it's a matter of the game
        # b - this is the correct answer
        # c - a variable entered for assignment capability
        a, b, c = result
        # Conclusion of the question
        print(a)
        answer = prompt.string('Your answer: ')
        if answer == str(b):
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is '{b}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f"Congratulations, {name}!")

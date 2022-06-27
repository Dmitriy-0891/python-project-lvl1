import prompt


ROUNDS_COUNTS = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE_GAME)
    for _ in range(ROUNDS_COUNTS):
        result = game.main()
        # a - it's a matter of the game
        # b - this is the correct answer
        a, b = result
        # Conclusion of the question
        print(a)
        answer = prompt.string('Your answer: ')
        if answer == b:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer:(. Correct answer is '{b}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f"Congratulations, {name}!")

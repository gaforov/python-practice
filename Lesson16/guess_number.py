import random


def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    print(f"\n{name}, let's play a game...")
    player_guess = input(
        '\nGuess which number I am thinking of... 1, 2, or 3.\n\n')

    if player_guess not in ['1', '2', '3']:
        print('\nPlease guess a number between 1, 2, or 3')
        return guess_number()

    player_guess = int(player_guess)
    computer_guess = random.randint(1, 3)

    print('\nI was thinking about the number', computer_guess)
    if player_guess != computer_guess:
        print('You chose', player_guess)

    if player_guess == computer_guess:
        print('You also chose', player_guess)
        print(f'\n🥳🥳🥳 You win, {name}! 🥳🥳🥳\n')
    else:
        print('\n🤖🤖🤖 Computer wins! 🤖🤖🤖\n')

    return guess_number


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalized game experience.'
    )

    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the person playing the game.'
    )

    args = parser.parse_args()

    guess_num = guess_number(args.name)
    # guess_num()

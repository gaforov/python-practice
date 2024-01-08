import random
import sys

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal game_count

        print(f"\n{name}, let's play a game...")
        player_guess = input('\nGuess which number I am thinking of... 1, 2, or 3.\n\n')

        if player_guess not in ['1', '2', '3']:
            print('\nPlease guess a number between 1, 2, or 3')
            return play_guess_number()

        player_guess = int(player_guess)
        computer_guess = random.randint(1, 3)

        print('\nI was thinking about the number', computer_guess)

        if player_guess != computer_guess:
            print('You chose', player_guess)

        if player_guess == computer_guess:
            player_wins += 1
            print(f"You also chose {player_guess} \n\n🥳🥳🥳 You win, {name}! 🥳🥳🥳\n")
        else:
            print(f"\nSorry, {name}. \n🤖🤖🤖 Computer wins! 🤖🤖🤖\n")

        game_count += 1
        print(f"Game count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"{name}'s win percentage: {player_wins/game_count:.2%}\n")

        print(f"\nPlay again, {name}?\n")

        while True:
            play_again = input('\nY for Yes or \nQ to Quit \n\n')
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break

        if play_again.lower() == 'y':
            return play_guess_number()
        else:
            print(f'\n🥳 🎉 Thanks for playing!')
            if __name__ == '__main__':
                sys.exit('🎮🎮🎮 Exiting the game...\n\n')
            else:
                return



    return play_guess_number


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
    guess_num()

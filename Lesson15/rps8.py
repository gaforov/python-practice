import random
import sys
from enum import Enum

# Adding ArgumentParser (command line) to make the game more personalized. 
# Note: To achieve this, you need to be 'in' the folder and run with command line, not play button. Ex: python3 rps8.py -n 'Said'


def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RockPaperScissors(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input(
            f'\n{name}, please enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n')

        if player_choice not in ['1', '2', '3']:
            print('\n{name}, please enter 1, 2, or 3. Try again.')
            return play_rps()

        # I could have converted in line 23 above but for accepting user input both for int and string this way is better.
        player = int(player_choice)

        computer = int(random.choice([1, 2, 3]))
        print(
            f"\n{name}, you chose: {str(RockPaperScissors(player)).replace('RockPaperScissors.', '')}")
        print(
            f"Computer chose: {str(RockPaperScissors(computer)).replace('RockPaperScissors.', '')}")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins

            if player == computer:
                return 'Tie game!'
            elif (
                (player == 1 and computer == 3) or
                (player == 3 and computer == 2) or
                (player == 2 and computer == 1)
            ):
                player_wins += 1
                return f'\n🥳🥳🥳 {name} wins! 🥳🥳🥳'
            else:
                computer_wins += 1
                return '\n🤖🤖🤖 Computer wins! 🤖🤖🤖'

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print('\nGame count:', game_count)
        print(f"\n{name}'s wins: {player_wins}")
        print('Computer wins:', computer_wins)

        print('\nPlay again?')

        while True:
            play_again = input('\nY for Yes or \nQ to Quit \n\n')
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break

        if play_again.lower() == 'y':
            return play_rps()
        else:
            print(f'\n🥳 🎉 Thanks for playing, {name}!')
            sys.exit('🎮🎮🎮 Exiting the game...\n\n')

    return play_rps


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

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()

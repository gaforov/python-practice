import random
import sys
from enum import Enum

# We are converting some prints to f-strings


def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal computer_wins

        class RockPaperScissors(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = input(
            '\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n')

        if player_choice not in ['1', '2', '3']:
            print('\nYou must enter 1, 2, or 3. Try again.')
            return play_rps()

        # I could have converted in line 14 but for accepting user input both for int and string this way is better.
        player = int(player_choice)

        computer = int(random.choice([1, 2, 3]))
        print(f"\nYou chose: {str(RockPaperScissors(player)).replace('RockPaperScissors.', '')}")
        print(f"Computer chose: {str(RockPaperScissors(computer)).replace('RockPaperScissors.', '')}")

        def decide_winner(player, computer):
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
                return '\n🥳🥳🥳 You win! 🥳🥳🥳'
            else:
                computer_wins += 1
                return '\n🤖🤖🤖 Computer wins! 🤖🤖🤖'

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print('\nGame count:', game_count)
        print('Your wins:', player_wins)
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
            print('\n🥳 🎉 Thanks for playing!')
            sys.exit('🎮🎮🎮 Exiting the game...\n\n')

    return play_rps


play = rps()

play()

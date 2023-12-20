import random
import sys
from enum import Enum

# We are adding scope to the game. 4th version/iteration. 
game_count = 0

def play_rps():
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
    print('\nYou chose:', str(RockPaperScissors(
        player)).replace('RockPaperScissors.', ''))
    print('Computer chose:', str(RockPaperScissors(
        computer)).replace('RockPaperScissors.', ''))

    def decide_winner(player, computer):
        if player == computer:
            return 'Tie game!'
        elif (
            (player == 1 and computer == 3) or
            (player == 3 and computer == 2) or
            (player == 2 and computer == 1)
        ):
            return '\n🥳🥳🥳 You win!'
        else:
            return '\n🤖🤖🤖 Computer wins!'
        
    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count
    game_count += 1

    print('\nPlayed games count:', game_count)

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


play_rps()

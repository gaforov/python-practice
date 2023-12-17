import random
import sys
from enum import Enum


class RockPaperScissors(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

play_again = True

while play_again:
    player = int(input('\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n'))
    while player < 1 or player > 3:
        player = int(input("You must enter 1, 2, or 3. Try gain.\n"))
    computer = int(random.choice([1, 2, 3]))
    print('\nYou chose:', str(RockPaperScissors(player)).replace('RockPaperScissors.', ''))
    print('Computer chose:', str(RockPaperScissors(computer)).replace('RockPaperScissors.', ''))
    # if player == 1 and computer == 3:
    #     print('🥳🥳🥳 You win!')
    # elif player == 2 and computer == 1:
    #     print('🥳🥳🥳 You win!')
    # elif player == 3 and computer == 2:
    #     print('🥳🥳🥳 You win!')
    # elif player == computer:
    #     print('🟰 Tie game!')
    # else:
    #     print('🤖🤖🤖 Coputer wins!')

    if player == computer:
        print('Tie game!')
    elif (
        (player == 1 and computer == 3) or
        (player == 3 and computer == 2) or
        (player == 2 and computer == 1)
    ):
        print('\n🥳🥳🥳 You win!')
    else:
        print('\n🤖🤖🤖 Computer wins!')


    play_again = input('\nPlay again? \nY for Yes \nPress any key to uit \n')
    if play_again.lower() == 'y':
        continue
    else:
        print('🥳 🎉 Thanks for playing!')
        # break
        play_again = False

sys.exit('🎮🎮🎮 Exiting the game...\n\n')
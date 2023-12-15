import random
import sys
from enum import Enum


class RockPaperScissors(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print()
player_choice = input(
    'Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n')

player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer = int(random.choice([1, 2, 3]))
# computer = int(computer_choice)

print()
print('You chose:', str(RockPaperScissors(player)).replace('RockPaperScissors.', ''))
print('Computer chose:', str(RockPaperScissors(computer)).replace('RockPaperScissors.', ''))
print()

if player == 1 and computer == 3:
    print('🥳 You win!')
elif player == 2 and computer == 1:
    print('🥳 You win!')
elif player == 3 and computer == 2:
    print('🥳 You win!')
elif player == computer:
    print('🟰 Tie game!')
else:
    print('🤖 Coputer wins!')

print()

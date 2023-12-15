import random

computer_choice = random.choice(['scissors', 'rock', 'paper']) 
user_choice = input('Do you want rock, paper, or scissors?\n')

print()
print('Computer chose:', computer_choice)
print('User chose:', user_choice)

# if user_choice == 'rock' and computer_choice == 'scissors':
#     print('You win!')
# elif user_choice == 'scissors' and computer_choice == 'paper':
#     print('You win!')
# elif user_choice == 'paper' and computer_choice == 'rock':
#     print('You win!')
# elif user_choice == computer_choice:
#     print('Tie game!')
# else:
#     print('Computer wins!')

# Optimize/refactor if-else organization
if user_choice == computer_choice:
    print('Tie game!')
elif (
    (user_choice == 'rock' and computer_choice == 'scissors') or
    (user_choice == 'scissors' and computer_choice == 'paper') or
    (user_choice == 'paper' and computer_choice == 'rock')
):
    print('You win!')
else:
    print('Computer wins!')

print()
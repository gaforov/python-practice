import random

def get_user_choice():
    user_choice = input('Enter your choice (rock, paper, or scissors):\n').lower()
    while user_choice.lower() not in ['rock', 'paper', 'scissors']:
        print('Invalid choice. Please enter "rock", "paper", or "scissors"')
        user_choice = input('\nEnter your choice:').lower()
        if user_choice == 'exit':
            break
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return('\nTie game!')
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return('\n🥳🥳🥳 You win!')
    else:
        return('\n🤖🤖🤖 Computer wins!')

def play_game():

    play_again = True

    while play_again:
        print("\nLet's play 'Rock, Paper, or Scissors' game!\n")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print('\nComputer chose:', computer_choice)
        print('You chose:', user_choice)

        winner = determine_winner(user_choice, computer_choice)
        print(winner)

        play_again = input('\nPlay again? \nY for Yes \nPress any key for quit')
        if play_again.lower() == 'y':
            continue
        else:
            print("🕹️🕹️🕹️ Thanks for playing! Exiting the game...")
            play_again = False



play_game()
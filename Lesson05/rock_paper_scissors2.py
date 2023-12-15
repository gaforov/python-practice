import random

def get_user_choice():
    user_choice = input('Enter your choice (rock, paper, or scissors):\n').lower()
    while user_choice.lower() not in ['rock', 'paper', 'scissors']:
        print('Invalid choice. Please enter "rock", "paper", or "scissors"')
        user_choice = input('Enter your choice:').lower()
        if user_choice == 'exit':
            break
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return('Tie game!')
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return('🥳 You win!')
    else:
        return('Oh, no 💻 Computer wins!')

def play_game():

    print()
    print("Let's play 'Rock, Paper, or Scissors' game!\n")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print('Computer chose:', computer_choice)
    print('User chose:', user_choice)

    winner = determine_winner(user_choice, computer_choice)

    print(winner)



play_game()
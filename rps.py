import random

# Function to get the user's choice
def get_user_choice():
    user_choice = input("Rock, Paper, or Scissors? ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Rock, Paper, or Scissors? ").lower()
    return user_choice

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != "yes":
        break

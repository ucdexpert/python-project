import random

# List of possible choices
choices = ["rock", "paper", "scissors"]

# Get player's choice and convert it to lowercase
player_choice = input("Enter rock, paper or scissors: ").lower()

# Get computer's choice randomly
computer_choice = random.choice(choices)

# Check if it's a tie
if player_choice == computer_choice:
    print(f"Both choices were {player_choice}. It's a tie!")

# Check if player wins
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"Player wins! {player_choice} beats {computer_choice}.")

elif player_choice == "paper" and computer_choice == "rock":
    print(f"Player wins! {player_choice} beats {computer_choice}.")

elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Player wins! {player_choice} beats {computer_choice}.")

# If none of the above conditions are met, computer wins
else:
    print(f"Computer wins! {computer_choice} beats {player_choice}.")


 
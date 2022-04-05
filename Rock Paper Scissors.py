import random

user_action = input("Enter a choice")
actions = ["rock", "paper", "scissors"]
compAction = random.choice(actions)
print(f"\nYou chose {user_action}, computer chose {compAction}.\n")

if user_action == compAction:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if compAction == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if compAction == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if compAction == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
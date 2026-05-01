import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
rounds = 0

while rounds < 3:
    user = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer:", computer)

    if user not in choices:
        print("Invalid input")
        continue

    if user == computer:
        print("It's a tie")
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        print("You win")
        user_score += 1
    else:
        print("Computer wins")
        computer_score += 1

    rounds += 1
    print("Score -> You:", user_score, "| Computer:", computer_score)

if user_score > computer_score:
    print("You won the game")
elif computer_score > user_score:
    print("Computer won the game")
else:
    print("Game tied")
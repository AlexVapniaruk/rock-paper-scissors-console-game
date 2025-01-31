import random


def get_choices():
  options = ["rock", "paper", "scissors"]
  player_choice = input("enter a choice (rock, paper, scissors: ")
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}

  return choices


def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    if computer == "paper":
      return "Paper covers rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win!"
    if computer == "scissors":
      return "Scissors cuts paper! You lose."
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    if computer == "rock":
      return "Rock smashes scissors! You lose."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
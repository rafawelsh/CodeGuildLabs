#7.rps.py
import random

def calc_winner(comp_choice, user_choice):
    defeats = {
        #key     value
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    if comp_choice == user_choice:
        return "Tie"
    elif defeats[comp_choice] == user_choice:
        return "Computer wins"
    else: #elif defeats[comp_choice] != user_choice:
        return "User wins"

while True:
    rps = ["rock", "paper", "scissors"]
    while True: #input validation
        user_choice = input("Rock, paper, scissors: ").strip().lower()
        if user_choice in rps:
            break
    computer_choice = random.choice(rps)
    print(computer_choice)
    winner = (calc_winner(computer_choice, user_choice))
    print(winner)

    #rematch if the user loses
    if winner == "computer wins" or winner == "Tie":
        #or if winner == ["computer wins", "Tie"]:
        while True:
            play_again = input("Do you want to play again: ").strip().lower()
            if play_again in ["yes", "no"]:
                break
        if play_again == "no": 
            break
    else:
        break

# print(calc_winner("rock", "rock"))
# print(calc_winner("rock", "scissors"))
# print(calc_winner("rock", "paper"))
# print(calc_winner("scissors", "rock"))
# print(calc_winner("scissors", "paper"))
# print(calc_winner("scissors", "scissors"))
# print(calc_winner("paper", "rock"))
# print(calc_winner("paper", "scissors"))
# print(calc_winner("paper", "paper"))

import random

#Scores
user_wins = 0
draw = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:     #Game script
    #User Decision
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue
    
    #Computer Decision
    random_number = random.randint(0, 2)    #Rock: 0, Paper: 1, Scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + '.')

    #Result Calculation
    if user_input == 'rock' and computer_pick == 'scissors':    #User Decision: Rock
        print("You won!")
        user_wins += 1

    elif user_input == 'paper' and computer_pick == 'rock':   #User Decision: Paper
        print("You won!")
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == 'paper':   #User Decision: Scissors
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:   #Case: Draw
        print("It's a Draw!")
        draw += 1

    else:   #Case: User Lose
        print("You lose!")
        computer_win += 1

print(f'Your Wins: {user_wins}\nDraw: {draw}\nComputer Wins: {computer_win}')
print("Goodbye!")
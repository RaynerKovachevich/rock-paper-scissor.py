import random

user_WINS = 0
computer_WINS = 0
ties_WINS = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
      break
   
    if user_input not in options: 
       continue
    
    random_number = random.randint(0,2)
    # rock: 0 paper: 1 scissor: 2
    computer_pick = options[random_number]
    print("Computer piked" , computer_pick + ".")
    
    if user_input == computer_pick:
       print("It's a tie!")
       ties_WINS += 1
       continue

    if user_input == "rock" and computer_pick == "scissors":
       print("You won!")
       user_WINS += 1
       
    elif user_input == "paper" and computer_pick == "rock":
       print("You won!")
       user_WINS += 1
       
    elif user_input == "scissors" and computer_pick == "paper":
       print("You won!")
       user_WINS += 1

    else:
       print("You lost!")
       computer_WINS += 1   

print("You won", user_WINS, "times.")
print("The Computer won", computer_WINS, "times.") 
print("There tied", ties_WINS, "times.")
print("Goodbye!")


       


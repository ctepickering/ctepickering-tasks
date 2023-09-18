import random #imports the random module

choices = ["rock", "paper", "scissors"] 
choice = input("please input your choice;'rock', 'paper' or 'scissors' : ")
randomchoice = random.choice(choices)

print("The computer chose " + randomchoice)
if choice == randomchoice: 
    print("Tie") 
elif ((choice == "rock" and randomchoice == "scissors") or (choice == "paper" and randomchoice == "rock") or (choice == "scissors" and randomchoice == "paper")):
    print("You win")
else: 
    print("You loose") 
#end if
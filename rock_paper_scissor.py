import random

computer = random.choice(['rock', 'paper', 'scissor'])

human = input("Rock/Paper/Scissor?\n")
if(human=="paper"): print("human wins")
elif(human=="scissor"): print("computer wins")
else: print("Its a draw")
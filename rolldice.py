import random

roll = random.randint(1,6)
human = int(input("Guess the number\n"))
print(roll)
if(human==roll): print("Human wins")
else: print("Computer wins")
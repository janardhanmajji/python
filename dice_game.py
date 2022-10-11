import random

def roll_dice():
    roll = random.randint(1,6) + random.randint(1,6)
    return roll

p1 = input("Enter player 1's name\n")
p2 = input("Enter player 2's name\n")

r1 = roll_dice()
r2 = roll_dice()

print(p1, 'rolled', r1)
print(p2, 'rolled', r2)

if(r1>r2): print(p1, 'wins')
elif(r1<r2) : print(p2, 'wins')
else : print('Its a tie')






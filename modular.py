# import math
# math.add(2,3)
# random
# randint
# choice
import random
# print(random.randint(1,10))
# fruit=("apple","orange","mango","grapes")
# print(random.choice(fruit))
# coin=("head","tail")
# print(random.choice(coin))

# Os 
# sys 
# time

ch=("rock","paper","scissor")
player="" 
while player not in ch:
    player=input("rock,paper or scissor ").lower()
computer=random.choice(ch)
if player==computer:
    print("tie")
elif ((player=="rock"and computer=="scissor"or computer=="paper")or 
     (player =="paper" and computer=="rock"or computer=="scisssor")or
     (player=="scissor" and computer=="paper"or computer=="rock")):
     print("player win",player)
else:
     print("computer win",computer)
#ruleo f game 
import random
gamerule=[["draw",'win','loss'],['lose','draw','win'],['win','lose','draw']]
choices=['rock','paper','scissos']
#test if user is paper, and computer is rock
'''print(gamerule[0][1])'''

user = int(input('please enter 0 - rock, 1-paper, 2-scissors'))
computer = random.randint(0,2)
print(f"you enter {choices[user]}")
print(f"computer chose {choices[computer]}")
print(gamerule[computer][user])
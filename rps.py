import random

def play():
    move= random.choice(['r','p','s'])
    user = input("'r' for Rock,'p' for paper and 's' for scissors:\n")
    if move != user:
        if (move == 'rock' and user == 'paper'):
            return("You Won!")
        elif (move == 'paper' and user == 'scissors'):
            return("You Won!")
        elif (move == 'scissors' and user == 'rock'):
            return("You Won!") 
        else:
            return("I won!")
    else:
        return("DRAW!")
    
print(play())
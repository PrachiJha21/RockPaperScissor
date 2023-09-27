import random
def play():
    computer= random.choice(['r','p','s'])
    user = input("'r' for Rock,'p' for paper and 's' for scissors:\n")
       
    if user == computer:
       return('Its a tie')
    
    elif is_win (user, computer):
        return "You Won!"
    
    return 'You Lost!'
    
def is_win(player, opponent):
        if(player == 'r' and opponent == 's') or (player == 'p' and opponent =='r') \
            or (player =='s' and opponent =='p'):
            return True
        
print(play()) 

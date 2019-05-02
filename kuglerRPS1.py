import random

symbols = ['rock', 'paper', 'scissors']
raw_input = ''
player_symbol = raw_input
computer_symbol = random.choice(symbols)

print ('Player:  ', player_symbol)
print ('Computer:  ', computer_symbol)
print 
print
if player_symbol == computer_symbol:
    print ('Tie!')
elif player_symbol == 'rock':

        if computer_symbol == 'paper':
            print ('Computer wins!')
        
        else:
            print ('You won!')
    
elif player_symbol == 'paper':

        if computer_symbol == 'rock':
            print ('You won!')

        else:
            print ('Computer wins!')
        
elif player_symbol == 'scissors':

        if computer_symbol == 'paper':
            print ('You won!')

        else:
            print ('Computer wins!')
else: print('Unsure what to do about symbol: ' + player_symbol)
    

import random

symbols = ['rock', 'paper', 'scissors']
player_symbol = input("What symbol would you like to play? ")

computer_symbol = random.choice(symbols)



print 
print ('Player: ', player_symbol) 
print ('Computer: ', computer_symbol)
print 
if player_symbol == computer_symbol:
        print ('TIE!')
elif player_symbol == 'rock':
    if computer_symbol == 'paper':
        print ('Computer wins.')
    else:
        print ('Player wins.')
elif player_symbol == 'paper':
    if computer_symbol == 'scissors':
        print ('Computer wins.')
    else:
        print ('Player wins.')
elif player_symbol == 'scissors':
    if computer_symbol == 'rock':
        print ('Computer wins.')
    else:
        print ('Player wins.')
else:
    print ('I dont know what to do with a ' + player_symbol + '. ( T ʖ̯ T)')
    
        

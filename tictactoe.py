import random
theboard = {'tl': ' ', 'tm': ' ', 'tr': ' ',
            'ml': ' ', 'mm': ' ', 'mr': ' ',
            'll': ' ', 'lm': ' ', 'lr': ' '}

moves  = list(theboard.keys())

def printboard(board):
    print(board['tl']+'|'+board['tm']+'|'+board['tr'])
    print('-+-+-')
    print(board['ml']+'|'+board['mm']+'|'+board['mr'])
    print('-+-+-')
    print(board['ll']+'|'+board['lm']+'|'+board['lr'])


turn = 'X'
for i in range(9):
    printboard(theboard)
    if turn == 'X':
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theboard[move]=turn
        turn = 'O'
    else:
        print('COMPUTER PLAYED:')
        move = moves[random.randint(0, 8)]
        theboard[move]=turn
        turn = 'X'
        
printboard()
    

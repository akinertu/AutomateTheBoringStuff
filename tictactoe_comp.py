import random
theboard = {'tl': ' ', 'tm': ' ', 'tr': ' ',
            'ml': ' ', 'mm': ' ', 'mr': ' ',
            'll': ' ', 'lm': ' ', 'lr': ' '} #dictionary

moves  = list(theboard.keys())
played = []

def printboard(board):
    print(board['tl']+'|'+board['tm']+'|'+board['tr'])
    print('-+-+-')
    print(board['ml']+'|'+board['mm']+'|'+board['mr'])
    print('-+-+-')
    print(board['ll']+'|'+board['lm']+'|'+board['lr'])

def checkwinner():
    if theboard['tl'] == theboard['tm'] == theboard['tr'] != ' ' or \
        theboard['ml'] == theboard['mm'] == theboard['mr'] != ' ' or \
        theboard['ll'] == theboard['lm'] == theboard['lr'] != ' ' or \
        theboard['tl'] == theboard['ml'] == theboard['ll'] != ' ' or \
        theboard['tm'] == theboard['mm'] == theboard['lm'] != ' ' or \
        theboard['tr'] == theboard['mr'] == theboard['lr'] != ' ' or \
        theboard['tl'] == theboard['mm'] == theboard['lr'] != ' ' or \
        theboard['tr'] == theboard['mm'] == theboard['ll'] != ' ':
        return True
    else:
        return False

turn = 'X'
for i in range(9):
    printboard(theboard)
    if checkwinner() is True:
        print (turn + 'won!')
        break
    else:
        if turn == 'X':
            print('Turn for ' + turn + '. Move on which space?')
            move = input()
            theboard[move]=turn
            moves.remove(move)
            turn = 'O'
        else:
            print('COMPUTER PLAYED:')
            move = random.choice(moves)
            theboard[move]=turn
            moves.remove(move)
            turn = 'X'
printboard(theboard)

    
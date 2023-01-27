#! python3
theboard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bpawn', '5h': 'bqueen', '3e': 'wking'}

empty_board = []
game_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

def boardgenerator():
    for i in range (1,9):
        for k in range (ord('a'),ord('i')):
            square = str(i) + str(chr(k))
            empty_board.append(square)
    return empty_board 
boardgenerator()


def isValidChessBoard(game):
    pieces = list(game.values())
    coordinates = list(game.keys())    
    num_white = 0
    num_black = 0
    if (pieces.count('bking') == 1 and pieces.count('wking') == 1 and
        pieces.count('bpawn') <= 8 and pieces.count('wpawn') <= 8):
        for i in range(len(pieces)):
            if (coordinates[i] in empty_board and str(pieces[i])[1:] in game_pieces and
                num_white <= 16 and num_black <= 16):
                if str(list(game.values())[i])[:1] == 'w':
                    num_white += 1
                elif str(list(game.values())[i])[:1] == 'b':
                    num_black += 1
                else:
                    print('error3')
                    break
            else:
                print('error2')
                break
        return True
    else:
        print('error1')
        return False
    
isValidChessBoard(theboard)

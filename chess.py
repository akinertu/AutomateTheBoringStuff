empty_board = []
def boardgenerator():
    for i in range (1,9):
        for k in range (ord('a'),ord('i')):
            square = str(i) + str(chr(k))
            empty_board.append(square)
    print(empty_board)   
boardgenerator()


            

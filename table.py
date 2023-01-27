import random
width = 9
height = 9

def random_move():
    move = random.randint(0,1)
    if move == 1:
        print(' #', end ='')
    else:
        print(' O', end ='')

for y in range(height):
    for x in range(width):
        random_move()
    print('')
    
import random
wins = 0
losses = 0
ties = 0

while True:
    print('wins: '+str(wins),'losses: '+str(losses),'ties: '+str(ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_1 = input()
        if player_1 == 'q':
            sys.exit() # Quit the program
        elif player_1 == 'r' or player_1 == 'p' or player_1 == 's':
            break
        print('Type one of r, p, s, or q.')
        
    if player_1 == 'r':
        print('ROCK versus...')
    elif player_1 == 'p':
        print('PAPER versus...')
    elif player_1 == 's':
        print('SCISSORS versus...')
    
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
        
    if player_1 == 'q':
        sys.exit() # Quit the program
    elif player_1 == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif player_1 == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_1 == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif player_1 == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif player_1 == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif player_1 == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif player_1 == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
print('Game ended')
    
    


import random
import sys

#step 1: starting information
print('Welcome to RPS!!!')
moves: dict = {'rock' : '🏔️',
               'paper' : '📰',
               'scissor' : '✂️'
               }
valid_moves: list[str] = list(moves.keys())

comp_score, your_score = 0, 0
#step 2: infinite loop -- user inputs
while True:
    user_move: str = input('Rock, Paper or Scissor>> ').lower()
    
    if user_move == 'exit':
        print(f'Your Score {your_score}')
        print(f'Computer score: {comp_score}')
        print('Thanks for playing!!!🙏')
        sys.exit()
        
    if user_move not in valid_moves:
        print('Invalid moves!!!:(')
        continue
    
    #deciding time
    comp_move: str = random.choice(valid_moves)
    
    print('------')
    print(f'you: {moves[user_move]}')
    print(f'Computer: {moves[comp_move]}')
    print('------')
    
    #check moves
    if user_move == comp_move:
        print('It is a tie')
    elif user_move == 'rock' and comp_move == 'scissor':
        print('You win!')
        your_score += 1
    elif user_move == 'scissor' and comp_move == 'paper':
        print('You win!')
        your_score += 1
    elif user_move == 'paper' and comp_move == 'rock':
        print('You win!')
        your_score += 1
    else:
        print('Computer wins!....')
        comp_score += 1
        
        

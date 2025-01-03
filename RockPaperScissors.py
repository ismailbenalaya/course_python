import random
import sys

# Step 1 : Starting Information

print('Welcome ro RPS !!!')

moves : dict = {'rock' : '🪨','paper': "📜", "scissors" : "✂️"}

valid_moves : list[str] = list(moves.keys())

# Step 2 : Infinite Loop :

while True :
    user_move :  str = input("Rock Paper or Scissors :").lower()
    # Rock -> rock == 'rook'

    if user_move =="exit" :
        print('Thanks for playing !!')
        sys.exit()

    if user_move not  in valid_moves :
        print('Invalid Move .....')
        continue
    # AI decide :
    ai_move : str = random.choice(valid_moves)
    print("-----------")
    print(f'You : {moves[user_move]}')
    print(f'AI : {moves[ai_move]}')
    print("----")
    # Check moves
    if user_move == ai_move :
        print('It is a tie !')
    elif user_move == 'rook' and ai_move == 'scissors' :
        print("You Win")
    elif user_move == 'scissors' and ai_move == 'paper':
        print("You Win")
    elif user_move == 'paper' and ai_move == 'rock':
        print("You Win")
    else :
        print("AI win !!")






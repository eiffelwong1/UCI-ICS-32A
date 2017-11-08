import connectfour


def tutorial():
    print('=============================================================================')
    print('Welcome to Connect four:')
    print('Players will just have to type in the colume number to place the checkers')
    print('Who connects 4 checkers in a row will win the game')
    print('This game also have a POP feature,')
    print('   where Player can take away their own checker from bottem')
    print('Using this feature, type "pop" followed with a space then colume number')
    print('Enjoy and have fun !!!')
    print('')
    print('example input: "pop 3" , "3", "6" ')
    print('')
    print('=============================================================================')

def print_game_board(game_board):
    '''prints the game board'''
    for num_of_col in range(1,connectfour.BOARD_COLUMNS):
        print(num_of_col , end='  ')
    print(connectfour.BOARD_COLUMNS)                #this ends with a \n
        
    for row_num in range(0,connectfour.BOARD_ROWS):
        for col_num in range(0,connectfour.BOARD_COLUMNS):
        #for col in game_board:
            col = game_board[col_num]
            if col[row_num] == 0 and col_num == connectfour.BOARD_COLUMNS-1:
                print('.')
            elif col[row_num] == 1 and col_num == connectfour.BOARD_COLUMNS-1:
                print('R')
            elif col[row_num] == 2 and col_num == connectfour.BOARD_COLUMNS-1:
                print('Y')
            elif col[row_num] == 0:
                print('.',end='  ')
            elif col[row_num] == 1:
                print('R',end='  ')
            elif col[row_num] == 2:
                print('Y',end='  ')
            else:
                print('?',end='  ')

def user_interface(game_state: connectfour.GameState):
    '''prints the user interface'''
    
    if game_state[1] == 2:
        print("Yellow player's turn")
    elif game_state[1] == 1:
        print("Red player's turn")
    
    print_game_board(game_state[0])

    print('please input the colume you want to drop to:')

def main()-> None:
    tutorial()
    
    game_state = connectfour.new_game()
    
    while True:             #keeps game running until said quite
        user_input = 0

        user_interface(game_state)
        
        while True:         #re-ask input when invalid
            user_input = input()
            if user_input.startswith('pop '):
                try:
                    game_state = connectfour.pop(game_state,int(user_input[4:])-1)
                    break
                except ValueError:
                    print('Invalid input, please retry')
                except connectfour.InvalidMoveError:
                    print('move Invalid, please retry')
            else:
                try:
                    user_input = int(user_input)
                    game_state = connectfour.drop(game_state, user_input -1)
                    print('Droping on '+str(user_input))
                    break
                except ValueError:
                    print('Invalid input, please retry')
                except:
                    print('Input ERROR, please retry')            


        winner = connectfour.winner(game_state)
        if winner != 0:
            print_game_board(game_state[0])
            if winner == 1:
                print('player Red WIN !!!')
                break
            elif winner == 2:
                print('player Yellow WIN !!!')
                break
            else:
                print('gameover, player Unknown WIN')
                
            
                
            


        
if __name__ == '__main__':
    main()

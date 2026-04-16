from Game import *
import pdb

NUMBER_OF_ROWS            = 6
NUMBER_OF_COLS            = 7
NUMBER_OF_RECURSIVE_CALLS = 1


class ConnectFourGame(Game) :

    """Creates the starting board"""
    def __init__(self) :
        # initialize the starting board
        self.initial = [['.'] * NUMBER_OF_COLS for _ in range(NUMBER_OF_ROWS)]



    """Returns True if there is a win state for the given piece"""
    def winning_move(self, board, piece):
        # Check horizontal locations for win
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(NUMBER_OF_ROWS):
                if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                    c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(NUMBER_OF_COLS):
            for r in range(NUMBER_OF_ROWS - 3):
                if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                    c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(NUMBER_OF_ROWS - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                        board[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(NUMBER_OF_COLS - 3):
            for r in range(3, NUMBER_OF_ROWS):
                if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                        board[r - 3][c + 3] == piece:
                    return True
        return False



    # ROW: indexing from top to bottom [5, 4, 3, 2, 1, 0]
    # COL: indexing from left to right [0, 1, 2, 3, 4, 5, 6]
    def display(self, state):
        """Print or otherwise display the state."""
        print()
        for row in range(NUMBER_OF_ROWS-1,-1,-1):
            print(row, "|\t",end='')
            for col in range(NUMBER_OF_COLS):
                print(state[row][col],"\t", end="")
            print("|")

        print("-----------------------------------------------------------------")
        print(" \t0\t1\t2\t3\t4\t5\t6")


    def is_valid_location(self, state, col):
        # If the requested column is outside of the valid range
        # Then it's invalid
        if col <0 or col >= NUMBER_OF_COLS:
            return False
        else:
            # If there is an empty slot in the topmost row of the requested column
            # Then there is at least one available space to drop the piece in that column
            return state[NUMBER_OF_ROWS - 1][col] == '.'


    def get_next_open_row(self, state, col):

        # Start scanning from the bottom row of the specified column
        # Return the first available spot        
        for r in range(NUMBER_OF_ROWS):
            if state[r][col] == '.':
                return r
        return NUMBER_OF_ROWS


    def drop_piece(self, state, row, col, piece):
        state[row][col] = piece


    def undo(self, state, move):
        row = self.get_next_open_row(state, move)
        state[row-1][move] = '.'
        return state



    def terminal_test(self, state):
        return self.winning_move(state, "x") or self.winning_move(state, "o") or len(self.actions(state)) == 0



    def actions(self, state):
        # returns list of numbers corresponding to possible moves
        valid_locations = []
        # your code
        a = 0
        while a <= NUMBER_OF_COLS:
            if(self.is_valid_location(state, a)):
                valid_locations += [a]
            a += 1
        return valid_locations

    
    def result(self, state, move, player):
        """Return the state that results from making a move from a state."""
        # you should modify your state[][] list and then return the modified one
        # your code
        row = self.get_next_open_row(state, move)
        state[row][move] = player
        return state
    

    def utility(self, state, player):
        """Return the value of this final state to player."""
        # your code
        # ...
        # ...
        # ...


    def get_opposite_player(self,player):
        # return the opposite of player
        if player == 'x':
            return 'o'
        else:
            return 'x'
    

    def minimax(self, state, player, depth=0):

        # HINT: call self.terminal_test() and or check depth
        # your code
        # ...
        # ...


        bestMove = -1

        # maximizing player (in our setup it's the AI)
        if player == 'o':

            best = -100000
            # your code
            # ...
            # ...
            # ...


        else:

            # minimizing player (in our setup it's human player)
            best = 1000000
            # your code
            # ...
            # ...
            # ...


        return best, bestMove



    def play(self, state):
        game_over = False
        turn = 1
        while not game_over:
            self.display(state)
            if turn == 1:
                print("HUMAN PLAYER")
                col = int(input("Where to drop a piece?"))
                if self.is_valid_location(state, col):
                    row = self.get_next_open_row(state, col)
                    self.drop_piece(state, row, col, 'x')
                    turn = 2
                else:
                    print('not a valid location; try again')

                if self.winning_move(state, 'x'):
                    print("Human player wins!")
                    game_over = True

            else:

                print("AI")
                val, col = self.minimax(state, "o", depth=4)


                #global NUMBER_OF_RECURSIVE_CALLS
                #print("number of recursive calls = ", NUMBER_OF_RECURSIVE_CALLS)
                if self.is_valid_location(state, col):
                    row = self.get_next_open_row(state, col)
                    self.drop_piece(state, row, col, 'o')
                    turn = 1
                else:
                    print('not a vaild location; try again')

                if self.winning_move(state, 'o'):
                    print("AI wins!")
                    game_over = True

            if self.terminal_test(state):
                game_over = True
        self.display(state)


# 2 player game
#play the game
game = ConnectFourGame()
game.play(game.initial)

#Reference
'''self.initial[row][column]'''
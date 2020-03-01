# Othello

# GLOBALS
GRID_SIZE = 8
# EASY for not generating moves; HARD for generating player moves till depth >= 3
DIFFICULTY = 'EASY'
BOARD = [[-1 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
WHITE_SCORE = 2
BLACK_SCORE = 2
# GLOBALS


def display_board():
    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            print(BOARD[i][j], end=' ')
        print()


def evaluation_function(black_count, white_count):
    return (black_count - white_count)


def modified_evaluation_function(arguments):
    # do crazy shit here if needed
    dummy = None

def is_adjacent(x, y, turn):
    opposite_piece = 1 - turn
    for i in range (x - 1, x + 2):
        for j in range (y - 1, y + 2):
            if (i >= 0 and i <= GRID_SIZE and j >= 0 and j <= GRID_SIZE):
                if (BOARD[i][j] == opposite_piece):
                    return True
    return False


def check_valid(x, y, turn):
    if (x >= GRID_SIZE or y >= GRID_SIZE):
        return False
    if (x < 0 or y < 0):
        return False
    # Black must place a black disc on the board, 
    # in such a way that there is at least one straight 
    # (horizontal, vertical, or diagonal) occupied line 
    # between the new disc and another black disc, with 
    # one or more contiguous white pieces between them. 
    return is_adjacent(x, y, turn) and BOARD[x][y] == -1


def continue_game():
    return (WHITE_SCORE + BLACK_SCORE < GRID_SIZE * GRID_SIZE)

def flip_pieces(x, y, turn):


def main():

    global BOARD
    global WHITE_SCORE
    global BLACK_SCORE

    initial_position = int((GRID_SIZE / 2) - 1)

    # white = 1
    # black = 0
    BOARD[initial_position][initial_position] = 1  # white top-left
    BOARD[initial_position + 1][initial_position + 1] = 1  # white bottom-right
    BOARD[initial_position][initial_position + 1] = 0  # black top-right
    BOARD[initial_position + 1][initial_position] = 0  # black bottom-left

    display_board()
    turn = 0
    while (continue_game() is True):

        valid_choice = False
        while(valid_choice != True):
            
            if (not turn):
                # human move
                choice_x = int(input("Enter x-coordinate for black: "))
                choice_y = int(input("Enter y-coordinate for black: "))
                # check if the player has entered a valid move
                valid_choice = check_valid(choice_x - 1, choice_y - 1, turn)
                if (valid_choice is False):
                    print("Invalid choice.")
                # update pieces <add code>
                BOARD[choice_x - 1][choice_y - 1] = 0 # update board with new move
                flip_pieces(choice_x - 1, choice_y - 1, turn)
                turn = not turn
            
            else:
                # AI's move
                # play with minmax 
                # <add code>
                turn = not turn

        display_board()

if __name__ == "__main__":
    main()

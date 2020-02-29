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


def check_valid(x, y):
    if (x > GRID_SIZE or y > GRID_SIZE):
        return False
    if (x < 0 or y < 0):
        return False
    return True  # FIX


def continue_game():
    return (WHITE_SCORE + BLACK_SCORE < GRID_SIZE * GRID_SIZE)


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
    
    while (continue_game() is True):

        valid_choice = False
        while(valid_choice is not True):
            choice_x = int(input("Enter x-coordinate for black: "))
            choice_y = int(input("Enter y-coordinate for black: "))
            # check if the player has entered a valid move
            valid_choice = check_valid(choice_x, choice_y)
            if (valid_choice is False):
                print("Invalid choice.")

        BOARD[choice_x - 1][choice_y - 1] = 0
        display_board()

if __name__ == "__main__":
    main()

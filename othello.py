#Othello

#GLOBALS
GRID_SIZE = 8
DIFFICULTY = 'EASY'  #EASY for not generating moves; HARD for generating player moves till depth >= 3
BOARD = [[-1 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)] 
#GLOBALS

def display_board():
    for i in range(0,GRID_SIZE):
        for j in range(0, GRID_SIZE):
           print(BOARD[i][j], end= ' ')
        print() 


def evaluation_function(black_count, white_count):
    return (black_count - white_count)


def modified_evaluation_function(arguments):
    #do crazy shit here if needed
    dummy = None


def main():
    
    global BOARD
    
    intial_position = int((GRID_SIZE / 2) - 1)

    BOARD[intial_position][intial_position] = 1 #white top-left
    BOARD[intial_position + 1][intial_position + 1] = 1 #white bottom-right
    BOARD[intial_position][intial_position + 1] = 0 #black top-right
    BOARD[intial_position + 1][intial_position] = 0 #black bottom-left

    
    display_board()

if __name__ == "__main__":
    main()
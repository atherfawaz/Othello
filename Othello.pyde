# Othello

# GLOBALS
GRID_SIZE = 8
# EASY for not generating moves; HARD for generating player moves till depth >= 3
DIFFICULTY = 'EASY'
BOARD = [[5 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
WHITE_SCORE = 2
BLACK_SCORE = 2
WIDTH = 70
turn = 0
INITIAL = True
# GLOBALS

#sets up the window size
def setup():
    size(800,800)
    initial_position = int((GRID_SIZE / 2) - 1)
    BOARD[initial_position][initial_position] = 1  # white top-left
    BOARD[initial_position + 1][initial_position + 1] = 1  # white bottom-right
    BOARD[initial_position][initial_position + 1] = 0  # black top-right
    BOARD[initial_position + 1][initial_position] = 0  # black bottom-left

#gets called whenever board is updated
def draw():
    x,y = 70,70
    for row in range(0, GRID_SIZE):
        for col in range(0, GRID_SIZE):
            if (BOARD[row][col] == 5):
                fill(200, 200, 200)
            elif(BOARD[row][col] == 1):
                # print white
                fill(255, 255, 255)
            elif(BOARD[row][col] == 0):
                # print black
                fill(0,0,0)
            rect(x, y, WIDTH, WIDTH)
            x += WIDTH
        y += WIDTH
        x = 70
        
def check_valid(x, y, turn, doFlipping):
    if (x >= GRID_SIZE or y >= GRID_SIZE):
        return False
    if (x < 0 or y < 0):
        return False
    # Black must place a black disc on the board,  in such a way that there is at least one straight (horizontal, vertical, or diagonal)
    # occupied line  between the new disc and another black disc, with one or more contiguous white pieces between them.
    return is_condition_satisfied(x, y, turn, doFlipping) and BOARD[x][y] == 5

def update_score():
    global WHITE_SCORE
    global BLACK_SCORE
    BLACK_SCORE = WHITE_SCORE = 0
    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            if (BOARD[i][j] == 0):
                BLACK_SCORE += 1
            elif (BOARD[i][j] == 1):
                WHITE_SCORE += 1

def possible_moves(turn):
    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            if (BOARD[i][j] == 5):
                valid_choice = check_valid(i, j, turn, False)
                if valid_choice is True:
                    return True
    return False

def continue_game():
    return (WHITE_SCORE + BLACK_SCORE < GRID_SIZE * GRID_SIZE)
     
def evaluation_function(black_count, white_count):
    return (black_count - white_count)


def modified_evaluation_function(arguments):
    # do crazy shit here if needed
    dummy = None

def is_flip_possible(x, y, oppX, oppY, turn, doFlipping):
    global BOARD
    check = {'L': False, 'R': False, 'U': False, 'D': False,
             'DR': False, 'DL': False, 'UR': False, 'UL': False}
    flippingPos = {'x': 0, 'y': 0}
    # opponent lies on left
    if oppX == x and oppY == y-1:
        for i in range(oppY-1, 0, -1):
            if BOARD[x][i] == turn:
                flippingPos['x'] = x
                flippingPos['y'] = i
                check['L'] = True
                break
        if (check['L'] and doFlipping):
            for i in range(oppY, flippingPos['y'], -1):
                BOARD[x][i] = turn
    # opponent lies on right
    if oppX == x and oppY == y+1:
        for i in range(oppY+1, GRID_SIZE):
            if BOARD[x][i] == turn:
                flippingPos['x'] = x
                flippingPos['y'] = i
                check['R'] = True
                break
        if (check['R'] and doFlipping):
            for i in range(oppY, flippingPos['y']):
                BOARD[x][i] = turn
    # opponent lies up
    if oppX == x-1 and oppY == y:
        for i in range(oppX-1, 0, -1):
            if BOARD[i][y] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = y
                check['U'] = True
                break
        if (check['U'] and doFlipping):
            for i in range(oppX, flippingPos['x'], -1):
                BOARD[i][y] = turn
    # opponent lies down
    if oppX == x+1 and oppY == y:
        for i in range(oppX+1, GRID_SIZE):
            if BOARD[i][y] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = y
                check['D'] = True
                break
        if (check['D'] and doFlipping):
            for i in range(oppX, flippingPos['x']):
                BOARD[i][y] = turn
    # opponent lies down-right
    if oppX == x+1 and oppY == y+1:
        i = oppX+1
        j = oppY+1
        while i != GRID_SIZE and i != 0 and j != GRID_SIZE and j != 0:
            if BOARD[i][j] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = j
                check['DR'] = True
                break
            i += 1
            j += 1
        if (check['DR'] and doFlipping):
            i = oppX
            j = oppY
            while i != flippingPos['x'] and j != flippingPos['y']:
                BOARD[i][j] = turn
                i += 1
                j += 1
    # opponent lies down-left
    if oppX == x+1 and oppY == y-1:
        i = oppX+1
        j = oppY-1
        while i != 0 and i != GRID_SIZE and j != GRID_SIZE and j != 0:
            if BOARD[i][j] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = j
                check['DL'] = True
                break
            i += 1
            j -= 1
        if (check['DL'] and doFlipping):
            i = oppX
            j = oppY
            while i != flippingPos['x'] and j != flippingPos['y']:
                BOARD[i][j] = turn
                i += 1
                j -= 1
    # opponent lies up-right
    if oppX == x-1 and oppY == y+1:
        i = oppX-1
        j = oppY+1
        while i != GRID_SIZE and i != 0 and j != GRID_SIZE and j != 0:
            if BOARD[i][j] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = j
                check['UR'] = True
                break
            i -= 1
            j += 1
        if (check['UR'] and doFlipping):
            i = oppX
            j = oppY
            while i != flippingPos['x'] and j != flippingPos['y']:
                BOARD[i][j] = turn
                i -= 1
                j += 1
    # opponent lies up-left
    if oppX == x-1 and oppY == y+1:
        i = oppX-1
        j = oppY-1
        while i != GRID_SIZE and i != 0 and j != GRID_SIZE and j != 0:
            if BOARD[i][j] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = j
                check['UL'] = True
                break
            i -= 1
            j -= 1
        if (check['UL'] and doFlipping):
            i = oppX
            j = oppY
            while i != flippingPos['x'] and j != flippingPos['y']:
                BOARD[i][j] = turn
                i -= 1
                j -= 1
    # return false if all false, else return true
    return not all(value == False for value in check.values())


def is_condition_satisfied(x, y, turn, doFlipping):
    opposite_piece = 1 - turn
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i >= 0 and i <= GRID_SIZE - 1 and j >= 0 and j <= GRID_SIZE - 1):
                if (BOARD[i][j] == opposite_piece):
                    if is_flip_possible(x, y, i, j, turn, doFlipping):
                        return True
    return False

def displayBoard():
    for row in BOARD:
        print(row)
    print(" ")

# this function gets called upon every mouse click
def mousePressed():
    global BOARD
    global turn
    if (continue_game() and possible_moves(turn) is True):
        if(check_valid(mouseY/WIDTH - 1, mouseX/WIDTH - 1, turn, True) is True):
            BOARD[mouseY/WIDTH - 1][mouseX/WIDTH - 1] = turn
            update_score()
            displayBoard()

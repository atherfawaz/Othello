# Othello
import copy

# GLOBALS
GRID_SIZE = 8
# EASY for not generating moves; HARD for generating player moves till depth >= 3
DIFFICULTY = 'HARD'
BOARD = [[5 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
validBoard = [[5 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
WHITE_SCORE = 2
BLACK_SCORE = 2
WIDTH = 70
turn = 0
INITIAL = True
gameFlag = True
switchCount = 0
invalidFlag = False
EXIT_ = False
MAX_DEPTH = 3
# GLOBALS

#sets up the window size
def setup():
    global DIFFICULTY
    if (GRID_SIZE == 3):
        DIFFICULTY = 'EASY'
    fullScreen()
    size(800,800)
    initial_position = int((GRID_SIZE / 2) - 1)
    BOARD[initial_position][initial_position] = 1  # white top-left
    BOARD[initial_position + 1][initial_position + 1] = 1  # white bottom-right
    BOARD[initial_position][initial_position + 1] = 0  # black top-right
    BOARD[initial_position + 1][initial_position] = 0  # black bottom-left
    possible_moves()

#gets called whenever board is updated
def draw():
    clear()
    background(255)
    global validBoard
    global EXIT_
    global gameFlag
    global invalidFlag
    global oppCheck
    x,y = 70,70    
    if gameFlag is True:
        if turn == 1:
            text("Click for opponent turn!",600,40)
        for row in range(0, GRID_SIZE):
            for col in range(0, GRID_SIZE):
                if (BOARD[row][col] == 5):
                    fill(200, 200, 200)
                    rect(x, y, WIDTH, WIDTH)
                    if (validBoard[row][col] == 3):
                        fill(0, 255, 0)
                        rect(x, y, WIDTH, WIDTH)
                elif(BOARD[row][col] == 1):
                    # print white
                    fill(200, 200, 200)
                    rect(x, y, WIDTH, WIDTH)
                    fill(255,255,255)
                    circle(x+35, y+35, 45)
                    if (validBoard[row][col] == 4):
                        fill(0, 0, 255)
                        circle(x+35,y+35,15)
                elif(BOARD[row][col] == 0):
                    # print black
                    fill(200,200,200)
                    rect(x, y, WIDTH, WIDTH)
                    fill(0,0,0)
                    circle(x+35, y+35, 45)
                x += WIDTH
            y += WIDTH
            x = 70
        textSize(32)
        fill(0, 0, 0)
        text("OTHELLO ", 10, 40)
        textSize(20)
        text("Black: ", 200, 40)
        text(BLACK_SCORE, 270, 40)
        text("White: ", 370, 40)
        text(WHITE_SCORE, 440, 40) 
        if invalidFlag is True:
            textSize(32)
            fill(255, 0, 0)
            text("INVALID MOVE",600, 40)
        else:
            possible_moves()
    else:
        textSize(32)
        fill(0, 0, 0)
        text("OTHELLO ", 10, 40)
        textSize(20)
        text("Black: ", 200, 40)
        text(BLACK_SCORE, 270, 40)
        text("White: ", 370, 40)
        text(WHITE_SCORE, 440, 40) 
        textSize(32)
        fill(255, 0, 0)
        if (WHITE_SCORE>BLACK_SCORE):
            s = "White Wins!"
        elif (WHITE_SCORE<BLACK_SCORE):
            s = "Black Wins!"
        else:
            s = "It was a tie."
        text("Game ended! " + s,1920/2-150,1080/2)
        delay(4000)
        EXIT_ = True
      
def mousePressed():
    global switchCount
    global BOARD
    global turn
    global invalidFlag
    global gameFlag
    global EXIT_
    global validBoard
    invalidFlag = False
    #possible_moves()
    #global INDICES
    print(mouseY/WIDTH, mouseX/WIDTH)
    if (continue_game() is True):
        if (switchCount == 1):
            print("here " + str(turn))
        if (turn == 0):
            # Player's turn
            if(check_valid(mouseY/WIDTH - 1, mouseX/WIDTH - 1, turn, True) is True):
                BOARD[mouseY/WIDTH - 1][mouseX/WIDTH - 1] = turn
                update_score()
                turn = 1 - turn
                switchCount = 0
                validBoard = [[5 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
            else:
                invalidFlag = True
        elif (turn == 1): 
            delay(800)
            if (switchCount == 1):
                print("here")
            turnVals = opponent_turn(DIFFICULTY,turn)
            if turnVals['check'] is True: 
                is_condition_satisfied(turnVals['x'], turnVals['y'],  turn, True)
                BOARD[turnVals['x']][turnVals['y']] = turn
                validBoard[turnVals['x']][turnVals['y']] = 4
                update_score()
                turn = 1 - turn
                switchCount = 0
    else:
        gameFlag = False
        if (EXIT_ is True):
            exit()
# Othello
import copy


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


def evaluation_function(black_count, white_count):
    return (white_count - black_count)


def min_max(depth, maxDepth, turn, isMax):
    global BOARD
    global BLACK_SCORE
    global WHITE_SCORE
    ORIG_BOARD = copy.deepcopy(BOARD)
    origBlackScore = BLACK_SCORE
    origWhiteScore = WHITE_SCORE

    alpha = float('-inf')
    beta = float('inf')

    turnVals = {'x': -1, 'y': -1, 'check': False, 'max_': -1000, 'min_': 1000}

    if depth >= maxDepth or (continue_game() is not True and (WHITE_SCORE>BLACK_SCORE)):
        tempTurnVals = {'x': -1, 'y': -1, 'check': False, 'max_': -1000, 'min': 1000} 
        tempTurnVals['max_'] = evaluation_function(BLACK_SCORE, WHITE_SCORE)
        tempTurnVals['min_'] = evaluation_function(BLACK_SCORE, WHITE_SCORE)
        return tempTurnVals
    if isMax:
        for i in range(0, GRID_SIZE):
            for j in range(0, GRID_SIZE):
                if check_valid(i, j, turn, True):
                    # BOARD[turnVals['x']][turnVals['y']] = turn
                    update_score()
                    #x = evaluation_function(BLACK_SCORE, WHITE_SCORE)
                    ORIG_BOARD = copy.deepcopy(BOARD)
                    origBlackScore = BLACK_SCORE
                    origWhiteScore = WHITE_SCORE
                    tempTurnVals = min_max(depth+1, maxDepth, 1-turn,not isMax)
                    if tempTurnVals['max_'] > turnVals['max_']:
                        turnVals['max_'] = tempTurnVals['max_']
                        turnVals['min_'] = tempTurnVals['min_']
                        turnVals['x'] = i
                        turnVals['y'] = j
                        turnVals['check'] = True
                BOARD = copy.deepcopy(ORIG_BOARD)
                BLACK_SCORE = origBlackScore
                WHITE_SCORE = origWhiteScore
        return turnVals
    if not isMax:
        for i in range(0, GRID_SIZE):
            for j in range(0, GRID_SIZE):
                if check_valid(i, j, turn, True):
                    # BOARD[turnVals['x']][turnVals['y']] = turn
                    update_score()
                    #x = evaluation_function(BLACK_SCORE, WHITE_SCORE)
                    ORIG_BOARD = copy.deepcopy(BOARD)
                    origBlackScore = BLACK_SCORE
                    origWhiteScore = WHITE_SCORE
                    tempTurnVals = {'x': -1, 'y': -1, 'check': False, 'max_': -1000, 'min_': 1000}
                    tempTurnVals = min_max(depth+1, maxDepth, 1-turn,isMax)
                    if tempTurnVals['min_'] < turnVals['min_']:
                        turnVals['min_'] = tempTurnVals['min_']
                        turnVals['max_'] = tempTurnVals['max_']
                        turnVals['x'] = i
                        turnVals['y'] = j
                        turnVals['check'] = True
                BOARD = copy.deepcopy(ORIG_BOARD)
                BLACK_SCORE = origBlackScore
                WHITE_SCORE = origWhiteScore
        return turnVals


def opponent_turn(DIFFICULTY,turn):
    max_ = -1000
    global BOARD
    global BLACK_SCORE
    global WHITE_SCORE
    ORIG_BOARD = copy.deepcopy(BOARD)
    origBlackScore = BLACK_SCORE
    origWhiteScore = WHITE_SCORE
    turnVals = {'x':-1,'y':-1,'check':False}
    if (DIFFICULTY == 'EASY'):
        for i in range(0,GRID_SIZE):
            for j in range(0,GRID_SIZE):
                if check_valid(i, j, turn, True):
                    BOARD[turnVals['x']][turnVals['y']] = turn
                    update_score()
                    x = evaluation_function(BLACK_SCORE,WHITE_SCORE)
                    BOARD = copy.deepcopy(ORIG_BOARD) 
                    BLACK_SCORE = origBlackScore
                    WHITE_SCORE = origWhiteScore
                    if x>max_:
                        max_ = x
                        turnVals['x']=i
                        turnVals['y']=j
                        turnVals['check']=True
    elif(DIFFICULTY == 'HARD'):
        # check to depth 3
        turnVals = min_max(1,MAX_DEPTH,turn,True)
    BOARD = copy.deepcopy(ORIG_BOARD) 
    BLACK_SCORE = origBlackScore
    WHITE_SCORE = origWhiteScore
    return turnVals                          


def is_flip_possible(x, y, oppX, oppY, turn, doFlipping):
    check = {'L': False, 'R': False, 'U': False, 'D': False,
             'DR': False, 'DL': False, 'UR': False, 'UL': False}
    flippingPos = {'x': 0, 'y': 0}
    # opponent lies on left
    if oppX == x and oppY == y-1:
        for i in range(oppY-1, -1, -1):
            if BOARD[x][i] == turn:
                flippingPos['x'] = x
                flippingPos['y'] = i
                check['L'] = True
                break
            if BOARD[x][i] == 5:
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
            if BOARD[x][i] == 5:
                break
        if (check['R'] and doFlipping):
            for i in range(oppY, flippingPos['y']):
                BOARD[x][i] = turn
    # opponent lies up
    if oppX == x-1 and oppY == y:
        for i in range(oppX-1, -1, -1):
            if BOARD[i][y] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = y
                check['U'] = True
                break
            if BOARD[i][y] == 5:
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
            if BOARD[i][y] == 5:
                break
        if (check['D'] and doFlipping):
            for i in range(oppX, flippingPos['x']):
                BOARD[i][y] = turn
    # opponent lies down-right
    if oppX == x+1 and oppY == y+1:
        i = oppX+1
        j = oppY+1
        while i < GRID_SIZE and i >= 0 and j < GRID_SIZE and j >= 0:
            if BOARD[i][j] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = j
                check['DR'] = True
                break
            if BOARD[i][j] == 5:
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
        while i < GRID_SIZE and i >= 0 and j < GRID_SIZE and j >= 0:
            if BOARD[i][j] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = j
                check['DL'] = True
                break
            if BOARD[i][j] == 5:
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
        while i < GRID_SIZE and i >= 0 and j < GRID_SIZE and j >= 0:
            if BOARD[i][j] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = j
                check['UR'] = True
                break
            if BOARD[i][j] == 5:
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
    if oppX == x-1 and oppY == y-1:
        i = oppX-1
        j = oppY-1
        while i < GRID_SIZE and i >= 0 and j < GRID_SIZE and j >= 0:
            if BOARD[i][j] == turn:
                flippingPos['x'] = i
                flippingPos['y'] = j
                check['UL'] = True
                break
            if BOARD[i][j] == 5:
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


def check_valid(x, y, turn, doFlipping):
    if (x >= GRID_SIZE or y >= GRID_SIZE):
        return False
    if (x < 0 or y < 0):
        return False
    # Black must place a black disc on the board,  in such a way that there is at least one straight (horizontal, vertical, or diagonal)
    # occupied line  between the new disc and another black disc, with one or more contiguous white pieces between them.
    return is_condition_satisfied(x, y, turn, doFlipping) and BOARD[x][y] == 5  


def continue_game():
    global switchCount
    if switchCount <= 2:
        return (WHITE_SCORE + BLACK_SCORE < GRID_SIZE * GRID_SIZE)
    else:
        return False

def flip_pieces(x, y, turn):
    dummy = None


def possible_moves():
    global validBoard
    global switchCount
    global turn
    valid = False
    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            if (BOARD[i][j] == 5):
                valid_choice = check_valid(i, j, turn, False)
                if valid_choice is True:
                    valid = True
                    if (turn == 0):
                        validBoard[i][j] = 3     
    if (valid == False):
        turn = 1 - turn 
        switchCount += 1
        print("Turn switched as no moves available " + str(switchCount) + "Turn is now: " + str(turn))
    return valid

def displayBoard():
    for row in BOARD:
        print(row)
    print(" ")

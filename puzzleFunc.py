FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4


def get_current_player(pone_turn):
    """ (bool) -> str """
   
    if pone_turn == True:
        return 'Player One'
    else:
        return 'Player Two'


def get_winner(pone_score, ptwo_score):
    """ (int, int) -> str """
   
    if pone_score > ptwo_score:
        return 'Player One Wins!'
    elif pone_score < ptwo_score:
        return 'Player Two Wins!'
    elif pone_score == ptwo_score:
        return 'Tie game!'


def get_factor(direction): 
    """ (str) -> int

    Precondition: direction (one of 'up', 'down', 'forward' and 'backward')
    """    
    # Return factor of direction
    if direction == 'up':
        return UP_FACTOR
    elif direction == 'down':
        return DOWN_FACTOR
    elif direction == 'forward':
        return FORWARD_FACTOR
    elif direction == 'backward':
        return BACKWARD_FACTOR
    
    
def get_points(direction, words_left):
    """ (str, int) -> int
    
    Precondition: direction (one of 'up', 'down', 'forward' and 'backward')
    """
    
    # Return point for guess
    # Words remaining to be guessed includes current guess
    if (1 < words_left < 5):
        return get_factor(direction) * (10 - words_left)    
    elif (words_left == 1):
        return get_factor(direction) * (10 - words_left) + 25
    elif (words_left >= 5):
        return get_factor(direction) * 5
    


def calculate_score(puzzle, direction, guess, row_or_col_num, words_left):
    """ (str, str, str, int, int) -> int """
    
    s = guess
    
    # If guess is found in that direction and in either row or column,
    # return appropriate score
    
    if not s.isalpha():
        return 0
    
    if direction == 'up' and\
       contains(get_column(puzzle, row_or_col_num), reverse(s)):
        return get_points(direction, words_left)
    elif direction == 'down' and\
         contains(get_column(puzzle, row_or_col_num), s):
        return get_points(direction, words_left)
    elif direction == 'forward' and\
         contains(get_row(puzzle, row_or_col_num), s):
        return get_points(direction, words_left)
    elif direction == 'backward' and\
         contains(get_row(puzzle, row_or_col_num), reverse(s)):
        return get_points(direction, words_left)
    else:
        return 0   

def get_row(puzzle, row_num):
    """ (str, int) -> str

    Precondition: 0 <= row_num < number of rows in puzzle
    """
    # Return row row_num
    rows = puzzle.strip().split('\n')
    return rows[row_num]


def get_column(puzzle, col_num):
    """ (str, int) -> str

    Precondition: 0 <= col_num < number of columns in puzzle
    """

    # Return column col_num
    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]
    
    return column


def reverse(s):
    """ (str) -> str """

    s_reversed = ''
    for ch in s:
        s_reversed = ch + s_reversed

    # Return reversed str
    return s_reversed


def contains(s1, s2):
    """ (str, str) -> bool """

    return s2 in s1

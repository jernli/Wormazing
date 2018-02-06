import puzzleFunc


def get_num_rows(puzzle):
    """ (str) -> int """

    return puzzle.count('\n')


def get_num_cols(puzzle):
    """ (str) -> int """

    return puzzle.index('\n')


def print_puzzle(puzzle):
    """ (str) -> NoneType """

    # Split puzzle into rows and get dimensions.
    puzzle_rows = puzzle.strip().split('\n')
    num_rows = get_num_rows(puzzle)
    num_columns = get_num_cols(puzzle)

    # Print the column headings, -1 for "\n".
    # Two spaces between each letter
    print('   ', end='')
    for col_number in range(num_columns-1):
        print(col_number, ' ', end='')

    print()

    # Print each row number and row.
    for row_number in range(num_rows):
        print(row_number, end='  ')
        print('  '.join(puzzle_rows[row_number]))

    print()


def print_words(words):
    """ (list of str) -> NoneType """

    print('The remaining words to be found: ')
    for word in words:
        print(word, end=' ')
    print('\n')


def get_direction_calculate_score(puzzle, guess, current_player_name, words):
    """ (str, str, str, str, list of str) -> int """

    # Prompt for the direction.
    direction = None
    while direction not in ['up', 'down', 'forward', 'backward']:
        direction = input(
            current_player_name +
            ', enter the direction (up, down, forward, or backward): ')

    # Prompt for the row or column number, check whether the word occurs in
    # that row or column in the direction specified, and calculate the score.
    if direction == 'up' or direction == 'down':
        row_or_col_num = int(
            input('Enter the column number where ' + guess + ' occurs: '))
    elif direction == 'forward' or direction == 'backward':
        row_or_col_num = int(
            input('Enter the row number where ' + guess + ' occurs: '))

    words_left = len(words)

    return Puzzle_func.calculate_score(
        puzzle, direction, guess, row_or_col_num, words_left)


def take_turn(puzzle, words, current_player_name):
    """ (str, list of str, str) -> int """
    
    num_rows = get_num_rows(puzzle)
    num_cols = get_num_cols(puzzle)

    # Prompt for a word from the list of valid words.
    guess = input(current_player_name + ', please enter a word: ').strip()

    # score is 0 if guess not in words
    score = get_direction_calculate_score(
        puzzle, guess, current_player_name, words)

    # Remove the guess from the word list.
    if (score != 0 and guess.isalpha()):
        words.remove(guess)
    else:
        print("Player One's guess did not match the word in puzzle!")

    # Return number of occurrences word in puzzle
    return score


def game_over(words):
    """ (list of str) -> bool """

    return len(words) == 0


def play_game(puzzle, words):
    """ (str, list of words) -> Nonetype """

    # Whether it's Player One's turn; if False, it's Player Two's turn.
    pone_turn = True

    # The scores for the two players.
    pone_score = 0
    ptwo_score = 0

    print('''***************************************
**       Where's That Word?          **
***************************************''')

    # Prompt for a guess and add up the points until the game is over.
    while not game_over(words):

        print_puzzle(puzzle)
        print_words(words)

        # Get the name of the player whose turn it is.
        current_player_name = \
            Puzzle_func.get_current_player(pone_turn)

        # Have the player take their turn and get the score.
        score = take_turn(puzzle, words, current_player_name)

        # Update the score for whoever's turn it is.
        if pone_turn:
            pone_score = pone_score + score
            print(current_player_name + "'s score is " +
                  str(pone_score) + '.\n')
        else:
            ptwo_score = ptwo_score + score
            print(current_player_name + "'s score is " +
                  str(ptwo_score) + '.\n')

        pone_turn = not pone_turn

    print(Puzzle_func.get_winner(pone_score, ptwo_score))



puzzle = """ umhctxdtuj
javahfsoty
ldfastetyp
aipyhrpnwc
mjuyhgyotr
cemarftryn
azgvjnhohf
qwdrhgotre
plaertnoms
rdgyhrcntv
"""

words = ['toronto', 'montreal', 'python', 'java', 'madi', 'frame']

play_game(puzzle, words)

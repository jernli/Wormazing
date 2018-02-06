'''To test the parameter and return types of functions. Type checks pass if
nothing is returned when run. '''

import puzzleFunc as pf

# Get the initial values of the constants
constants_before = [pf.FORWARD_FACTOR, pf.DOWN_FACTOR, pf.BACKWARD_FACTOR,
                    pf.UP_FACTOR]


# Type check pf.get_current_player
result = pf.get_current_player(True)
assert isinstance(result, str), \
       '''pf.get_current_player should return a str, but returned {0}
       .'''.format(type(result))


# Type check pf.get_winner
result = pf.get_winner(17,32)
assert isinstance(result, str), \
       '''pf.get_winner should return a str, but returned {0}.''' \
       .format(type(result))


# Type check pf.get_factor
result = pf.get_factor('forward')
assert isinstance(result, int), \
       '''pf.get_factor should return an int, but returned {0}.''' \
       .format(type(result))


# Type check pf.get_points
result = pf.get_points('up', 7)
assert isinstance(result, int), \
       '''pf.get_points should return an int, but returned {0}.''' \
       .format(type(result))


# Type check pf.calculate_score
result = pf.calculate_score('abcd\nefgh\nijkl\n', 'forward', 'bcd', 2, 4)
assert isinstance(result, int), \
       '''pf.calculate_score should return an int, but returned {0}.''' \
       .format(type(result))


# Get the final values of the constants
constants_after = [pf.FORWARD_FACTOR, pf.DOWN_FACTOR, pf.BACKWARD_FACTOR,
                    pf.UP_FACTOR]
# Check whether the constants are unchanged.
assert constants_before == constants_after, \
       '''Your function(s) modified the value of a constant(s).'''
    

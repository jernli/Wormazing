'''To test the parameter and return types of functions.'''

import unittest
import puzzleFunc as pf

class TestTypes(unittest.TestCase):
    
    # Get the initial values of the constants
    constants_before = [pf.FORWARD_FACTOR, pf.DOWN_FACTOR, pf.BACKWARD_FACTOR,
                        pf.UP_FACTOR]
    
    
    # Type check pf.get_current_player
    def test_get_current_player(self):
        result = pf.get_current_player(True)
        self.assertIsInstance(result, str), \
            '''pf.get_current_player should return a str, but returned {0}
            .'''.format(type(result))
    
    
    # Type check pf.get_winner
    def test_get_winner(self):
        result = pf.get_winner(17,32)
        self.assertIsInstance(result, str), \
            '''pf.get_winner should return a str, but returned {0}.''' \
            .format(type(result))
    
    
    # Type check pf.get_factor
    def test_get_factor(self):
        result = pf.get_factor('forward')
        self.assertIsInstance(result, int), \
            '''pf.get_factor should return an int, but returned {0}.''' \
            .format(type(result))
    
    
    # Type check pf.get_points
    def test_get_points(self):
        result = pf.get_points('up', 7)
        self.assertIsInstance(result, int), \
            '''pf.get_points should return an int, but returned {0}.''' \
            .format(type(result))
    
    
    # Type check pf.calculate_score
    def test_calculate_score(self):
        result = pf.calculate_score('abcd\nefgh\nijkl\n', 'forward', 'bcd', 2, 4)
        self.assertIsInstance(result, int), \
            '''pf.calculate_score should return an int, but returned {0}.''' \
            .format(type(result))
    
    
    # Get the final values of the constants
    def test_constant_after(self):
        constants_after = [pf.FORWARD_FACTOR, pf.DOWN_FACTOR, pf.BACKWARD_FACTOR,
                           pf.UP_FACTOR]
    # Check whether the constants are unchanged.
        self.assertEqual(TestTypes.constants_before, constants_after), \
            '''Function(s) modified the value of a constant(s).'''

if __name__ == '__main__':
    unittest.main(exit=False)
            
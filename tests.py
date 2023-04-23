import unittest
import games
import algorithm
from fractions import Fraction

class ShapleyTest(unittest.TestCase):

    def test_small_bankruptcy_game(self):
        self.assertEqual(algorithm.Shapley(games.BankruptcyGame(9, [2,3,5,7])), [Fraction(13,12),Fraction(19,12),Fraction(31,12),Fraction(15,4)])





if __name__ == "__main__":
    unittest.main()




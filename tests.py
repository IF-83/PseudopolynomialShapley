import unittest
import games
import algorithm
from fractions import Fraction
import random
import brute_force

class ShapleyTest(unittest.TestCase):

    def test_small_bankruptcy_game(self):
        self.assertEqual(algorithm.Shapley(games.BankruptcyGame(9, [2,3,5,7])), [Fraction(13,12),Fraction(19,12),Fraction(31,12),Fraction(15,4)])

    def test_small_symmetric_voting_game(self):
        number_of_players, weight, quota = 5, 2, 8
        g = games.VotingGame([weight]*number_of_players, quota)
        sh = [Fraction(1,number_of_players)] * number_of_players 
        self.assertEqual(algorithm.Shapley(g), sh)
        
    def test_large_symmetric_voting_game(self):
        number_of_players, weight, quota = 20, 1, 8
        g = games.VotingGame([weight]*number_of_players, quota)
        sh = [Fraction(1,number_of_players)] * number_of_players 
        self.assertEqual(algorithm.Shapley(g), sh)

    def test_random_symmetric_voting_games(self):
        for _ in range(10):
            with self.subTest():
                number_of_players, weight = random.randint(5, 15), random.randint(1,2)
                quota = random.randint(3, number_of_players * weight-1)
                g = games.VotingGame([weight]*number_of_players, quota)
                sh = [Fraction(1,number_of_players)] * number_of_players
                self.assertEqual(algorithm.Shapley(g), sh)
    
    def test_random_voting_games(self):
        for _ in range(15):
            with self.subTest():
                number_of_players = random.randint(5, 15)
                weights = random.choices([1,2,3,4,5,6,7,8,9], k = number_of_players)
                quota = random.randint(3, sum(weights)-1)
                g = games.VotingGame(weights, quota)
                sh = brute_force.brute_force_voting_game(weights, quota)
                self.assertEqual(algorithm.Shapley(g), sh)




if __name__ == "__main__":
    unittest.main()




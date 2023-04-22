# A linear representation of a TU game is a set of weights, denoted by a_i (i in N) and a function that calculates the value of a coalition based on the sum of its weights.

class Game:
    def __init__(self, a:'list[int]', f:'callable[int,int]'):
        self.a = a
        self.f = f


class BankruptcyGame(Game):
    def __init__(self, assets: int, liabilities:'list[int]'):
        total_liabs = sum(liabilities)
        super().__init__([assets]+liabilities, lambda x: max([0, x - (total_liabs - assets)]))


class VotingGame(Game):
    def __init__(self, weights, quota):
        super().__init__(weights, lambda x: 1 if x >= quota else 0)


if __name__ == "__main__":
    try:
        general_game = Game([1,2,3,4], lambda x : x)
        print(f"Game {general_game} has been created.")
        bankruptcy_game = BankruptcyGame(9, [2,3,5,7])
        print(f"Bankruptcygame {bankruptcy_game} has been created.")
        print(f"Testing the function: f(4) = {bankruptcy_game.f(4)}, and f(10) = {bankruptcy_game.f(10)}.")
        voting_game = VotingGame([1,2,3,4,5,6], 10)
        print(f"Voting game {voting_game} has been created.")
        print(f"Testing the function: f(4) = {voting_game.f(4)}, and f(15) = {voting_game.f(15)}.")
        print("OK")
    except:
        raise Exception("Unexpected error occurred.")


        


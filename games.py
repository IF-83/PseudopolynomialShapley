# A linear representation of a TU game is a set of weights, denoted by a_i (i in N) and a function that calculates the value of a coalition based on the sum of its weights.

class Game:
    def __init__(self, a:'list[int]', f:'callable[int,int]'):
        self.a = a
        self.f = f


class BankruptcyGame(Game):
    def __init__(self, assets: int, liabilities:'list[int]'):
        total_liabs = sum(liabilities)
        super().__init__([assets]+liabilities, lambda x: max([0, x - (total_liabs - assets)]))






if __name__ == "__main__":
    try:
        general_game = Game([1,2,3,4], lambda x : x)
        print(f"Game {general_game} has been created.")
        bankruptcy_game = BankruptcyGame(9, [2,3,5,7])
        print(f"Bankruptcygame {bankruptcy_game} has been created.")
        print(f"Testing the function: f(4) = {bankruptcy_game.f(4)}, and f(10) = {bankruptcy_game.f(10)}.")
    except:
        raise Exception("Unexpected error occurred.")


        


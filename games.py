# A linear representation of a TU game is a set of weights, denoted by a_i (i in N) and a function that calculates the value of a coalition based on the sum of its weights.

class Game:
    def __init__(self, a:'list[int]', f:'callable[int,int]'):
        self.a = a
        self.f = f










if __name__ == "__main__":
    try:
        tu_game = Game([1,2,3,4], lambda x : x)
        print(f"Game {tu_game} has been created.")
    except:
        raise Exception("Unexpected error occurred.")


        


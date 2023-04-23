from itertools import combinations
from fractions import Fraction

def brute_force_voting_game(w: 'list[int]', q:int) -> 'list[int]':
    n = len(w)
    N = [i for i in range(n)]
    SH = []
    for player in N:
        N_1 = [i for i in N if i != player]
        sh = 0
        n_k = 1
        for k in range(n):
            for S in combinations(N_1, k):
                wS = sum(w[j] for j in S)
                sh += Fraction(int((wS + w[player] >= q) - (wS >= q)),n_k)
            n_k *= n - 1 - k
            n_k //= k + 1
        SH.append(Fraction(sh,n))
    return SH


if __name__ == "__main__":
    Shapley_value = brute_force_voting_game([4,4,4,2,2,1], 12)
    for s in Shapley_value:
    	print(s, end = " ")
    print("")
    for s in Shapley_value:
    	print(round(float(s), 5), end = " ")
    print("")

    	


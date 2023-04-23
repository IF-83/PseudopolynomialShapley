from fractions import Fraction
from numpy.polynomial import Polynomial
from sortedcontainers import SortedSet
from collections import defaultdict


def base_polynomials(arr: 'list[int]') -> 'tuple[dict[Polynomial], list[int]]':
    """Takes the weights of the linear representation of a TU-game, (arr) and calculates the base polynomials. Returns a dictionary of the polynomials and a sorted list of keys for the nonzero polynomials."""
    polynomials = {0: Polynomial([Fraction(1)])}
    x = Polynomial([Fraction(0),Fraction(1)])
    keys = SortedSet([0])
    for a in arr:
        poly_tmp = defaultdict(Fraction)
        for i in polynomials:
            j = i + a
            poly_tmp[i] += polynomials[i] * (1 - x)
            poly_tmp[j] += polynomials[i] * x
            keys.add(j)
        polynomials = poly_tmp
    return keys, polynomials


def decompose(base_poly, a:int) -> 'list[Polynomial]':
    """Inverts the last step of the base polynomial calculation. Returns a list of polynomials that can be used to calculate the Shapley value of the player with weight a."""
    x = Polynomial([Fraction(0),Fraction(1)])
    P = {}
    keys, poly = base_poly
    for k in keys:
        i = k - a
        if i in keys:
            P[k] = (poly[k] - P[i]*x)//(1-x)
        else:
            P[k] = poly[k]//(1-x)
    return P


def Shapley(game: 'Game') -> 'list[int]':
    arr = game.a
    B = base_polynomials(arr)
    Sh = []
    for a in arr:
        pols = decompose(B, a)
        p = sum([(game.f(j+a)-game.f(j))*pols[j] for j in pols])
        coefs = p.coef
        deg = len(coefs) - 1
        sh = sum([Fraction(coefs[i],i+1) for i in range(1,deg+1)])
        Sh.append(sh)
    return Sh


if __name__ == "__main__":
    import games
    l, A = [2,3,5,7], 9
    bg = games.BankruptcyGame(A, l)
    S = Shapley(bg)
    for s in S:
        print(s, end = ", ")
    print("")
    for s in S:
        print(round(float(s),5), end = ", ")
    print("") 
    
    
        



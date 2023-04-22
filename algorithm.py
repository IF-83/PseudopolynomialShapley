from fractions import Fraction
from numpy.polynomial import Polynomial
from sortedcontainers import SortedSet
from collections import defaultdict


def base_polynomials(arr: 'list[int]')-> 'tuple[dict[Polynomial], list[int]]':
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


if __name__ == "__main__":
    b = base_polynomials([2,3,5,7])
    for k in b[0]:
        print(k, "->", b[1][k])
    


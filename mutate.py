from typing import List, Dict


def find_order_with_most_books_scanned(L, D, L_signuptimes, L_shipperday):
    def weighting(l):
        a1, a2 = 1., 1.
        return a1 * L_signuptimes[l] + a2 * L_shipperday[l]
    return sorted(L, key=weighting)


def mutate(L: List[int], books: Dict[List[int]], D, L_signuptimes, L_shipperday):
    L = find_order_with_most_books_scanned(L, D, L_signuptimes, L_shipperday)
    return L, books

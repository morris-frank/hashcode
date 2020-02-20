def fitness(L, books, D, B_scores, L_signuptimes, L_shipperday):
    assert len(books) == len(L)

    score = 0.

    d = 0
    for l in L:
        d += L_signuptimes[l]
        number_of_books = (D - d) * L_shipperday[l]
        score += sum(books[l][:number_of_books])

    return score

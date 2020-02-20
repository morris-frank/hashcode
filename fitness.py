# Do this at beginning of new training
def setup_active_library_list(L, D, L_signuptimes):
    # Contains list of active libraries on that day (filling up)
    active_libs = [[] for _ in range(D)]
    i = 0
    for l in L:
        i += L_signuptimes[l]
        if i >= D:
            break
        for j in range(i, D):
            active_libs[j].append(l)
    return active_libs


# Optimization function, active_libs comes from above
def fitness(L, books, D, B_scores, L_signuptimes, L_shipperday):
    assert len(books) == len(L)
    scanned_books = set()

    active_libs = setup_active_library_list(L, D, L_signuptimes)

    score = 0.
    for d in range(D):
        for lib in active_libs[d]:
            for _ in range(L_shipperday[lib]):
                book = books[lib].pop(0)
                if book not in scanned_books:
                    scanned_books.add(book)
                    score += B_scores[book]
    return score



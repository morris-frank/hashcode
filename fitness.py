from collections import defaultdict


def fitness(L, books, D, B_scores, L_signuptimes, L_shipperday):
    assert len(books) == len(L)
    scanned_books = set()

    i_L = defaultdict(int)

    score = 0.
    waiting = False
    setupp = 0
    active_libs = []
    il = 0
    for d in range(D):
        if not waiting:
            if il < len(L):
                weiting_l = L[il]
                setupp = L_signuptimes[weiting_l]
                il += 1
                waiting = True
        for lib in active_libs:
            for _ in range(L_shipperday[lib]):
                if i_L[lib] < len(books[lib]) - 1:
                    book = books[lib][i_L[lib]]
                    if book not in scanned_books:
                        scanned_books.add(book)
                        score += B_scores[book]
                    i_L[lib] += 1
        if waiting:
            setupp -= 1
            if setupp == 0:
                active_libs.append(weiting_l)
                waiting = False

    return score



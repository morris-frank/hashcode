from typing import List, Dict


setup_times = dict()  # lib id ⇒ time to setup
scanning_n = dict()  # lib id ⇒ num of books scannable
scores = dict()  # book id ⇒ score
D = 100  # number of days


# Do this at beginning of new training
def setup_active_library_list(L: List[int], D: int):
    # Contains list of active libraries on that day (filling up)
    active_libs = [[] for _ in range(D)]
    i = 0
    for l in L:
        i += setup_times[l]
        for j in range(i, D):
            active_libs[j].append(l)
    return active_libs


# Optimization function, active_libs comes from above
def fitness(L: List[int], books: Dict[List[int]], active_libs):
    assert len(books) == L
    scanned_books = set()

    score = 0.
    for d in range(D):
        for lib in active_libs[d]:
            for _ in scanning_n[lib]:
                book = books[lib].pop(0)
                if book not in scanned_books:
                    scanned_books.add(book)
                    score += scores[book]
    return score



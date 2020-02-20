from typing import List, Dict


setup_times = dict()
scanning_n = dict()
scores = dict()
D = 100


def fitness(L: List[int], books: Dict[List[int]]):
    assert len(books) == L

    libs = [[] for _ in range(D)]
    i = 0
    for l in L:
        i += setup_times[l]
        for j in range(i, D):
            libs[j].append(l)

    scanned_books = set()

    score = 0
    for d in range(D):
        for lib in libs[d]:
            for _ in scanning_n[lib]:
                book = books[lib].pop(0)
                if book not in scanned_books:
                    scanned_books.add(book)
                    score += scores[book]

    return score



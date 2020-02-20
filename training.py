from collections import defaultdict
from argparse import ArgumentParser
from os.path import abspath
import random

from fitness import fitness
from mutate import mutate
from read_in import read_in
from saving import save_submission
from heuristic_1 import improve


def main(file):
    n_iter = 10000000

    B_scores, L_books, L_signuptimes, L_shipperday, D, B_id_set, L_id_set = read_in(
        file)
    library_books_sorted = defaultdict(list)

    for l, _books in L_books.items():
        library_books_sorted[l] = sorted(_books, key=lambda i: B_scores[i], reverse=True)

    max_score = 0.
    max_individual = None

    L = []
    n_sign_up_days_temp = 0
    L_choices = list(L_id_set)
    while (n_sign_up_days_temp < D) and len(L_choices) > 0:
        l_i = random.choice(L_choices)
        L_choices.remove(l_i)
        L.append(l_i)
        n_sign_up_days_temp += L_signuptimes[l_i]

    not_L = L_choices

    d = 0
    books = defaultdict(list)
    _book_sets = defaultdict(set)
    for l in L:
        d += L_signuptimes[l]
        n_scans_per_lib = (D - d) * L_shipperday[l]
        j = 0
        while len(books[l]) < n_scans_per_lib:
            j += 1
            book = random.choice(L_books[l])
            if book not in _book_sets[l]:
                books[l].append(book)
                _book_sets[l].add(book)
            if j >= 5 * len(L_books[l]):
                break

    max_L, max_books = L, books
    for it in range(n_iter):
        improve(L, books, L_signuptimes, L_shipperday, D)
        #print("HEre", flush=True)
        L, books, not_L, score = mutate(max_L.copy(), max_books.copy(), D, L_signuptimes, L_shipperday, not_L, library_books_sorted)
        #score = fitness(L, books, D, B_scores, L_signuptimes, L_shipperday)
        score = sum([B_scores[s] for s in score])
        #print(f"iter={it}, score={score}")

        if score > max_score:
            max_score = score
            print("New max", max_score)
            max_L, max_books = L, books
            save_submission(max_L, max_books, "max_ind")

    save_submission(max_L, max_books)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', type=abspath)

    args = parser.parse_args()
    main(args.f)

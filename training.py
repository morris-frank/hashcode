from argparse import ArgumentParser
from os.path import abspath

from .fitness import fitness
from .mutate import mutate
from .read_in import read_in


def main(file):
    n_iter = 100

    B_scores, L_books, L_signuptimes, L_shipperday, D, B_id_set, L_id_set = read_in(
        file)

    max_score = 0.
    max_individual = None
    for it in range(n_iter):
        L, books = mutate(L, books)

        score = fitness(L, books, D, B_scores, L_signuptimes, L_shipperday)

        if score > max_score:
            max_score = score
            max_individual = (L.copy(), books.copy())

    print(max_individual)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', type=abspath)

    args = parser.parse_args()
    main(args.file)

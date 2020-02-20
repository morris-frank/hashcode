from read_in import read_in
import numpy as np


def sorting_agent(file_name):
    data = read_in(file_name)
    B_scores, L_books, L_signuptimes, L_shipperday, D, B_id_set, L_id_set = data

    w_sup, w_d, w_sc = -2, 2, 2

    _scores = []
    for lib in L_id_set:
        signup = L_signuptimes[lib]
        shipday = L_shipperday[lib]
        lib_score = np.mean([B_scores[b_id] for b_id in L_books[lib]])
        _score = w_sup * signup + w_d * shipday + w_sc * lib_score

        b_id_sc = [(b_id, B_scores[b_id]) for b_id in L_books[lib]]
        b_id_sc.sort(key=lambda r: r[1], reverse=True)
        b_id_sc = [b_tuple[0] for b_tuple in b_id_sc]

        _scores.append((lib, _score, b_id_sc))

    _scores.sort(key=lambda r: r[1])

    print(_scores)

    libraries = []
    L_books_sol = {}
    for lib, _score, b_id_sc in _scores:
        libraries.append(lib)
        L_books_sol[lib] = b_id_sc

    return libraries, L_books_sol


if __name__ == "__main__":
    sorting_agent('a_example.txt')
    # sorting_agent('b_read_on.txt')

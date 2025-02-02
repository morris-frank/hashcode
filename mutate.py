import random

from heuristic_1 import get_best_book_order


def find_order_with_most_books_scanned(L, D, L_signuptimes, L_shipperday):
    def weighting(l):
        a1, a2 = 1., 1.
        return a1 * L_signuptimes[l] + a2 * L_shipperday[l]
    return sorted(L, key=weighting)

#library books sorted are list of lists, rows are library_id and cols are books_ids from big to small score
def mutate(L, books, D, L_signuptimes, L_shipperday, not_L, library_books_sorted):
    #L = find_order_with_most_books_scanned(L, D, L_signuptimes, L_shipperday)
    
    sum_of_L_days = sum([L_signuptimes[l] for l in L])
    random_r = random.random()
    if random_r < 0.5 and len(not_L) > 0:
        l_to_remove = random.randint(0, len(L)-1)        
        del books[L[l_to_remove]]
        not_L.append(L[l_to_remove])
        L.pop(l_to_remove)
        while sum_of_L_days < D:
            l_to_add = random.randint(0, len(not_L)-1)
            library_i_to_add = not_L[l_to_add]
            
            not_L.pop(l_to_add)
            L.append(library_i_to_add)
            sum_of_L_days += L_signuptimes[library_i_to_add]
    else:
        l_to_switch_1 = random.randint(0, len(L)-1)
        l_to_switch_2 = random.randint(0, len(L)-1)
        l_i = L[l_to_switch_1]
        L[l_to_switch_1] = L[l_to_switch_2]
        L[l_to_switch_2] = l_i
    books, new_fit = get_best_book_order(L, D, library_books_sorted, L_shipperday)


    return L, books, not_L, new_fit

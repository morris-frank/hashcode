import math

def get_best_book_order(libs_order, n_days, library_books_sorted, library_books_per_day):
    added_books = set()
    res = {}
    current_day = 0
    for l in libs_order:
        books_sorted = library_books_sorted[l]

        books_added = []
        
        n_books_per_day = library_books_per_day[l]
        current_day_temp = current_day
        added_books_this_day = 0
        
        for i, book_i in enumerate(books_sorted):
            if book_i not in added_books:
                books_added.append(book_i)
                added_books_this_day += 1
                added_books_this_day = added_books_this_day % n_books_per_day
                if added_books_this_day == 0:
                    current_day_temp += 1
                    if current_day_temp == n_days:
                        break
        res[l] = books_added
        added_books |= set(books_added)
    return res, added_books

def improve(L, books, L_signuptimes, L_booksrate, D):
    current_time = 0
    for i, l in enumerate(L[0:len(L)-1]):
        if current_time + L_signuptimes[L[i + 1]] + (len(books[l]) / L_booksrate[l]) < D:
            going_up_l = L[i]
            L[i] = L[i + 1]
            L[i+1] = going_up_l
        current_time += L_signuptimes[L[i]]
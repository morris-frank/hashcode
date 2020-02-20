import math

def get_best_book_order(libs_order, n_days, library_books_sorted, library_books_per_day):
    added_books = set()
    res = []
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
        res.append(books_added)
        added_books |= set(books_added)
    return res, added_books

def improve(L, books, L_signuptimes, L_booksrate):
    current_time = 0
    for i, l in enumerate(L):
        while(True):       
            if current_time + L_signuptimes[l] + (len(books[l]) / L_booksrate):
                pass
# book key: library id; value ordered list book ids

# Not tested
def save_submission(L, B, filename):
    """
    L: ordered list of library ids 
    B: dict l_id -> ordered list of books sent in time
    """
    # Assume tuple of library list and book id
    no_signed_libs = len(L)

    # Open a file with access mode 'a'
    with open(filename,'w+') as file_object:
        file_object.write(str(no_signed_libs) + '\n')
        for lib_id in L:
            books = B[lib_id]
            no_books_scanned = len(books)
            book_string = " ".join(str(x) for x in books)
            file_object.write(str(lib_id) +" "+ str(no_books_scanned) + '\n')
            file_object.write(str(book_string) + '\n')

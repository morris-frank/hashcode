# book key: library id; value ordered list book ids

# Not tested
def save_submission(individuals):
    # Assume tuple of library list and book id
    libraries, book_dict = individuals
    no_signed_libs = len(libraries)

    # Open a file with access mode 'a'
    with open("submission.txt", "a") as file_object:
        file_object.write(str(no_signed_libs) + '\n')
        for lib_id in libraries:
            books = book_dict[lib_id]
            no_books_scanned = len(books)
            book_string = " ".join(str(x) for x in books)
            file_object.write(str(lib_id) + str(no_books_scanned) + '\n')
            file_object.write(str(book_string) + '\n')

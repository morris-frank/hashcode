def read_in(filename):
    
    def replace_n_split(x):
        return [int(i) for i in x.replace('\n', '').split(' ')]

    with open(filename) as file:
        lines = [l for l in file.readlines() if not l=='\n']        
        B, L, D = replace_n_split(lines[0])
        B_scores = {i: b for i,b in enumerate(replace_n_split(lines[1]))}
        
        L_books = {}
        L_signuptimes = {}
        L_shipperday = {}
        
        for i in range(2, len(lines), 2):
            L_ID = int(i/2 -1)
            # sign up time, ship per day
            _, L_SUT, L_SPD = replace_n_split(lines[i])
            L_signuptimes[L_ID] = L_SUT
            L_shipperday[L_ID] = L_SPD

            L_BOOKS = replace_n_split(lines[i+1])
            L_books[L_ID] = L_BOOKS
            
    B_id_set = set(range(len(B_scores)))
    L_id_set = set(range(len(L_books)))

    return B_scores, L_books, L_signuptimes, L_shipperday, D, B_id_set, L_id_set



from read_in import read_in 
from saving import save_submission

def solve_b():
    B_scores, L_books, L_signuptimes, L_shipperday, D, B_id_set, L_id_set = read_in("b_read_on.txt")

    # same num of books with same scores
    L_sut = sorted(L_signuptimes.items(),key=lambda x:(x[1],x[0])) 
    
    res_l = []
    res_b = {}

    time = 0
    for idx, (l_id, sut) in enumerate(L_sut):

        time+=sut

        if time >= D:
            break 

        res_l.append(l_id)
        res_b[l_id] = L_books[l_id][:D-time]
    
    save_submission(res_l, res_b, "solution_b.txt")
        
    return 


def sort_by_averge(books, L_signuptimes, L_shipperday):
    sorted_L = [i for i in range(0, len(L_signuptimes))]
    sorted_L.sort(key=lambda x: L_signuptimes[x] + , reversed=True)
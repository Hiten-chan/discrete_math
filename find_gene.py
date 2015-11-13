def find_gene(lst, start):
    out_lst = lst[:]
    for  i, e in enumerate(lst):
        lst[i] = abs(e - start)
    m = lst.index(min(lst))
    return out_lst[m]

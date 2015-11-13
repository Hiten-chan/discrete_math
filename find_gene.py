def find_gene(lst, start):
    out_lst = lst[:]
    m = abs(lst[0] - start)
    for  i, e in enumerate(lst):
        lst[i] = abs(e - start)
        if lst[i] < m:
            m = lst[i]
    n = lst.index(m)
    return out_lst[n]

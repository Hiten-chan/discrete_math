def find_gene(lst, start):
    out_lst = lst[:]
    m = abs(lst[0] - start)
    for i in range(0, len(lst)):
        lst[i] = abs(lst[i] - start)
        if lst[i] < m:
            m = lst[i]
    n = lst.index(m)
    return out_lst[n]

def merge(a, b):
    c = []
    i = 0
    j = 0
        
    while i != len(a) and j != len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i != len(a):
        c.append(a[i])
        i += 1
    while j != len(b):
        c.append(b[j])
        j += 1
        
    return c


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    lst[:int(len(lst)/2)] = merge_sort(lst[:int(len(lst)/2)])
    lst[int(len(lst)/2):] = merge_sort(lst[int(len(lst)/2):])
    lst = merge(lst[:int(len(lst)/2)], lst[int(len(lst)/2):])
    return lst

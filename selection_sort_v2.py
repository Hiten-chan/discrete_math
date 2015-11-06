# selection_sort_variant_2

def selection_sort_v2(x):
    y = []
    while int(len(x)) > 1:
        key = x[0]
        k = 0
        for i in range(1, int(len(x))):
            if x[i] < key:
                k = i
                key = x[i]
        y.append(key)
        del x[k]
    return y

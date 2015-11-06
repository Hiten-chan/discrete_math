# selection sort

def selection_sort(x):
    y = []
    l = int(len(x))
    for i in range(0, l):
        key = x[i]
        k = i
        for j in range(i + 1, l):
            if x[j] < key:
                k = j
                key = x[j]
        x[k] = x[i]
        x[i] = key
        y.append(key)
    return y

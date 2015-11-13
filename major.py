def major(a):
    e = a[0]
    count = 1
    for i in range(1, len(a)):
        if a[i] == e:
            count += 1
        else:
            count -= 1
            if count == -1:
                e = a[i]
                count = 1
# addition code
    n = 0
    for x in a:
        if e == x:
            n += 1
    if n < len(a)/2:
        e = None
    return e

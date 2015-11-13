def part_sums(a):
    s = []
    s.append(a[0])
    for  i in range(1, len(a)):
        s.append(s[i-1] + a[i])
    return s

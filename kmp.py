# the Knuth–Morris–Pratt string searching algorithm

def pref_fun(x):
    d = {0:0}
    for i in range(1,len(x)):
        j = d[i-1]
        while j > 0 and x[j] != x[i]:
            j = d[j-1]
        if x[j] == x[i]:
            j += 1
        d[i] = j
    return d

def kmp(s, x):
    d = pref_fun(x)
    i = j = 0
    while i < len(s) and j < len(x):
        if x[j] == s[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = d[j-1]
    else:
        if j == len(x):
            return i - j 
        return None

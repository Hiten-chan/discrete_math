# binary search for sorted array

def bin_search(a, key):
    l = 0
    r = int(len(a) + 1)
    
    if key > a[int(len(a))-1]:
        return -1
    else:
        while l < r - 1:              
            m = int((l + r) / 2)            
            if a[m] < key:
                l = m
            else: 
                r = m 

        if a[r] == key:
            return r     
        elif a[0] == key:
            return 0
        else:
            return -1

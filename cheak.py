def cheak(a):
    counter_1 = 0
    counter_2 = 0
    for i in range(0, len(a)):
        if a[i] == '(':
            counter_1 += 1
        elif a[i] == '{':
            counter_2 += 1 
        elif a[i] == ')':
            counter_1 -= 1
        elif a[i] == '}':
            counter_2 -= 1
        if counter_1 < 0 or counter_2 < 0:
            return False
    return counter_1 == 0 and counter_2 == 0

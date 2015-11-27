# Пусть нам дана скобочная последовательность, записанная в строку a. 
# Возьмем переменные counter_1 = 0 и counter_2 = 0, которые будут отражать "баланс скобок". 
# Будем последовательно перебирать все символы строки a. 
# Если мы встречаем открывающую скобку вида "(", то увеличиваем counter_1 на 1.
# Если мы встречаем открывающую скобку вида "{", то увеличиваем counter_2 на 1.
# Если мы встречаем закрывающую скобку вида ")", то уменьшаем counter_1 на 1.
# Если мы встречаем закрывающую скобку вида "}", то уменьшаем counter_2 на 1.
# Если на протяжении всего перебора переменные counter_1 и counter_2 были 
# неотрицательными (не встречалось закрывающих скобок, для которых не было соответствующих открывающих), 
# и после завершения цикла переменные остались = 0 (все открывающие скобки закрыты, при этом нет лишних закрытых скобок), 
# то скобочная последовательность правильна. 

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

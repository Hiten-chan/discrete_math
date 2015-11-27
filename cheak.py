class Stack:
    
    def __init__(self, l):
        self.items = [0 for x in range(l)]
        self.i = 0
        
# Добавляет элемент в стек     
    def push(self, e):
        if self.i == len(self.items):
            print ("Стек полный")
        else:
            self.items[self.i] = e
            self.i += 1
    
# Удалить число с верхушки стека (последенее число)
    def pop(self):
        self.i -= 1
        
# Длина стека      
    def size(self):
        return(self.i)
    
# Проверка стека на пустоту   
    def IsEmpty(self):
        if self.i == 0:
            return True
        else:
            return False
            
# Вернуть последний добавленный элемент         
    def top(self):
        return self.items[self.i-1]
    
    
def cheack(s):
    st_1 = Stack(len(s))
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{':
            st_1.push(s[i])
        else:
            if st_1.IsEmpty() == True:
                return False
            elif s[i] == ')' and st_1.top() == '(':
                st_1.pop()
            elif s[i] == '}' and st_1.top() == '{':
                st_1.pop()
            else:
                return False
    return st_1.IsEmpty()

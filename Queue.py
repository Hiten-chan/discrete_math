# Очередь на основе двух стеков
# Операции empty, size и push не имеют циклов и не зависят от длины подаваемого списка => выполняются за O(1)
# Операция pop имеет 1 цикл и в лучшем случае она выполняется за O(1), но если self.leftStack
# не пустой, то операция pop может выполняться за O(n)

class Queue:
    
    def __init__(self, n):
        self.leftStack = [0 for x in range(n)]
        self.i_left = 0
        self.rightStack = [0 for x in range(n)]
        self.i_right = 0
        
        
    def empty(self):
        return self.i_left == self.i_right
    
    
    def size(self):
        if self.i_right > self.i_left:
            return n - elf.i_right + self.i_left
        else:
            return self.i_left - self.i_right
    
    
    def push(self, e):
        if self.i_left == len(self.leftStack):
            print ("Full")
        else:
            self.leftStack[self.i_left] = e
            self.i_left += 1
            
            
    def pop(self):
        if self.i_right == 0:
            if self.i_left == 0:
                return 'Empty'
            else:
                while self.i_left != 0:
                    self.rightStack[self.i_right] = self.leftStack[self.i_left - 1]
                    self.i_left -= 1
                    self.i_right += 1
        self.i_right -= 1
        return self.rightStack[self.i_right]

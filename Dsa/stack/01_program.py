from collections import deque

class Stack:
    def __init__(self):
        self.data = deque()

    def push(self, data):
        self.data.append(data)
    
    
    def pop(self):
        return self.data.pop()
        
    def peek(self):
        return self.data[-1]
    
    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return len(self.data) == 0
    
s = Stack()

s.push(2)
s.push(11)
s.push(34)
s.push(45)


print(s.data)
print(s.pop())
print(s.peek())
print(s.isEmpty())
print("After operations:",s.data)

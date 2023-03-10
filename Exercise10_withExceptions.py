"""
Define 3 categories of exceptions and make use of them
in the class Stack to indicate a problemn is encountered 
(Stack is full, Stack is empty, Wrong Stack size ...)

"""
class StackSizeError(Exception):
    pass
class StackFullError(Exception):
    pass
class StackEmptyError(Exception):
    pass

class Stack:
    
    def __init__(self, size):
        
        if isinstance(size, int) and size > 0:
            self.maxi=size
            self.data=[]
        else:
            raise StackSizeError(f"Wrong size given: {size} !")
            
    def __repr__(self): # (3/10) [20,56,45]
        return f"({len(self.data)}/{self.maxi}) {self.data}"
    
    def __eq__(self, other):
        return self.maxi == other.maxi and self.data == other.data
    
    def __len__(self):
        return len(self.data)
    
    def push(self, element):
        if len(self) < self.maxi:
            self.data.append(element)
        else:
            raise StackFullError("Push error: the Stack is full!")
            
    def pop(self):
        if len(self)>0:
            return self.data.pop()
        else:
            raise StackEmptyError("Pop error: the Stack is empty!")
            
    def peek(self):
        if len(self)>0:
            return self.data[-1]
        else:
            raise StackEmptyError("Peek error: the Stack is empty!")

if __name__ == "__main__":
    try:
        s1=Stack(2) # a new Stack with a max size of 10 elements
        s1.push(20)
        s1.push(56)
        s1.push(45)
        
        print(s1) # (3/10) [20,56,45]
        print(len(s1)) # print(s1.__len__()) 3
        
        top=s1.pop()
        print(top) # 45
        print(s1) # (2/10) [20,56]
        top=s1.pop()
        print(top) # 56
        print(s1) # (1/10) [20]
        top=s1.peek()
        print(top) # 20
        print(s1) # (1/10) [20]
    except Exception as ex:
        print("Exception received:",ex)

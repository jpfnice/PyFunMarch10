
class Stack:
    """
    Stack: mutable collection, with a fixed maximum size.

    Attributes:
        maxi: an int that represent the maximum size of the Stack
        data: a list to hold the elements pushed into the Stack
    Methods:
        __init__()
        push(element)
        __repr__()
        __len__()
        pop()
        peek()
        __eq__()
    """
    def __init__(self, size):
        """
        Parameters
        ----------
        size : TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        """
        if isinstance(size, int) and size > 0:
            self.maxi=size
            self.data=[]
        else:
            print("Wrong size given")
            
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
            print("The Stack is Full!")
            
    def pop(self):
        if len(self)>0:
            return self.data.pop()
        else:
            print("The Stack is Empty!")
            
    def peek(self):
        if len(self)>0:
            return self.data[-1]
        else:
            print("The Stack is Empty!")

if __name__ == "__main__":
    s1=Stack(10) # a new Stack with a max size of 10 elements
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

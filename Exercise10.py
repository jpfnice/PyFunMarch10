
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

class Stack:
    pass

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


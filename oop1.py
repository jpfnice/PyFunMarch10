import math

class Point: # __new__(), __init__(), __repr__(), __eq__()...
    def __init__(self, valx, valy): # A constructor
        self.x=valx # definition of the attribute x
        self.y=valy # definition of the attribute y
    def __repr__(self): # should return string
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y)
        if isinstance(other, int):
            return Point(self.x+other, self.y+other)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def distance(self, other):
        return math.sqrt((other.y-self.y)**2 + (other.x-self.x)**2)
    def clear(self):
        self.x=0
        self.y=0
        
# data=[5,6,7]
# data.append(18) # append(data, 18)

# l1=[2,3]
# l2=[5,6]
# l3=l1.__add__(l2)
# print(l3.__repr__())  


p1=Point(2,3)
# 1) p1=Point.__new__()
# 2) p1.__init__(2,3)
# 3) __init__(p1,2,3)

p2=Point(4,5)

print(p1) # <2,3>
# 1) print(str(p1))
# 2) print(p1.__repr__())

print(p2) # <4,5>

print(p1.x) # 2
p1.x=7
print(p1) # <7,3>

p3=p1+p2
# 1) p3=p1.__add__(p2)

print(p3) # <11, 8>

p3=p1+12
# 1) p3=p1.__add__(10)

print(p3) # <19, 15>
p1.x=p2.x=1
p1.y=2
p2.y=10
print(p1, p2)
if p1 == p2: # if p1.__eq__(p2):
    print("Equal")
    
result=p1.distance(p2)
print(result)

p1.clear()
print(p1) # <0,0>



# Inheritance
class ListPlus(list): # ListPlus "inherit from" list
     """
     list is the "super class" (or "mother class" ot "base class") of ListPlus
     ListPlus is a "sub class' (or "child class" or "derived class") of list
     """
     def removeAll(self, value):
         while value in self:
             self.remove(value)
             
     def __add__(li1, li2, default=0):
         li1_tmp=li1.copy() # li1_tmp=li1[:]
         li2_tmp=li2.copy()
         
         if len(li1) < len(li2):
             li1_tmp.extend([default]*(len(li2)-len(li1)))
             
         elif len(li2) < len(li1):
             li2_tmp.extend([default]*(len(li1)-len(li2)))   
         
         res=ListPlus()
         ix=0
         while ix < len(li1_tmp):
             res.append(li1_tmp[ix]+li2_tmp[ix])
             ix=ix+1
              
         return res
     
l1=ListPlus()
l1.append(12)
l1.append(13)
l1.append(14)
l1.append(12)
l1.append(23)
l1.append(12)
l1.append(12)
print(l1)

l2=ListPlus()
l2.append(2)
l2.append(3)
l2.append(4)
l2.append(5)
l2.append(10)

# l3=l1.addList(l2)
# print(l3)

l3=l1+l2
print(l3)
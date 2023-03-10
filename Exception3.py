

data=[56, 67, 89, 89, 98]


ix=input("Enter an int in the range [0,4]: ")

try:
    ix=int(ix)
    print(f"At position {ix} in data we do have {data[ix]}")
except ValueError as e:
    print("A ValueError is raised", e)
except IndexError as e:
    print("An IndexError is raised", e) 
except: # concerns the other kind of exceptions
    print("Other exceptions")
finally:
    print("Finally block")    
    
print("The end")

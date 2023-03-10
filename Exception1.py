

data=[56, 67, 89, 89, 98]


ix=input("Enter an int in the range [0,4]: ")

try:
    ix=int(ix)
    print(f"At position {ix} in data we do have {data[ix]}")
except:
    print("An exception is raised")
    
print("The end")
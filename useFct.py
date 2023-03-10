import myCode

try:
    result=myCode.subtract(5,"abc")
    print(result)
except Exception as e:
    print("Problem calling subtract:", e)
    
    
print("The end")
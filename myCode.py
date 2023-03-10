
def subtract(op1, op2):
    if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
        temp=op1 - op2 # temp is a local variable
        return temp
    else:
        raise Exception("Wrong kind of arguments received")



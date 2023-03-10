
"""
dict: a mutable collection
"""
phone={"Marco":23455, "Julia":45665,
       "Roman":76554}
print(phone)

print(phone["Julia"])
if "Jule" in phone:
    print(phone["Jule"])
else:
    print("Jule is not int the dict 'phone'")
    
phone["Julia"]=67666
print(phone["Julia"])
print(phone.get("Julia"))

phone["Yan"]=89888
print(phone, len(phone))

for name in phone:
    print(name,"-->", phone[name])

for pair in phone.items():
    print(pair)

for k,v in phone.items():
    print(k, v)

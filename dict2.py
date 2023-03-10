
"""
dict: a mutable collection
"""
#phone=dict() # To create an empty dict
phone={"Marco":[23455], "Julia":[45665, 67666],
       "Roman":[76554], "Marius":[]}
print(phone)

print(phone["Julia"])
if "Jule" in phone:
    print(phone["Jule"])
else:
    print("Jule is not int the dict 'phone'")
    
phone["Julia"].append(78776)

print(phone["Julia"])
print(phone.get("Julia"))

phone["Yan"]=[89888]
print(phone, len(phone))

for name in phone:
    print(name,"-->", phone[name])

for pair in phone.items():
    print(pair)

for k,v in phone.items():
    print(k, v)

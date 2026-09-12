s=input("Enter a string: ")
allowed="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
flag=True

for ch in s:
    if ch not in allowed:
        flag=False
        break
if flag:
    print("String contains only a-z, A-Z and 0-9")
else:
    print("String contains other characters")
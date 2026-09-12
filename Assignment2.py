a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
if a>b and a>c:
    print("The largest number is:", a)
elif b>a and b>c:
    print("The largest number is:", b)
elif c>a and c>b:
    print("The largest number is:", c)
else:
    print("All numbers are equal")
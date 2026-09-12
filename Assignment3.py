def right_triangle(a, b, c):
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("The triangle is a right-angled triangle.")
    else:
        print("The triangle is not a right-angled triangle.")
a=int(input("Enter the 1st side of the triangle: "))
b=int(input("Enter the 2nd side of the triangle: "))
c=int(input("Enter the 3rd side of the triangle: "))
right_triangle(a, b, c)
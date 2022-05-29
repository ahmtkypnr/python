from cmath import atan


def is_triangle(a,b,c):
    if(a+b>c and a+c>b and b+c>a):
        print("Yes")
    else:
        print("No")

a = int(input("First's length = "))
b = int(input("Second's length = "))
c = int(input("Third's length = "))

is_triangle(a,b,c)


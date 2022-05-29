import math
# def area(radius):
#     temp = math.pi * radius**2
#     return temp

# def distance(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1
#     dsquared = dx**2 + dy**2
#     result = math.sqrt(dsquared)
#     return result

# def circle_area(xc,yc,xp,yp):
#     radius = distance(xc,yc,xp,yp)
#     result = area(radius)
#     return result           #Başka bir fonksiyon diğerinin içinde çağırılabilir COMPOSİTİON

# def circle_area(xc, yc, xp, yp):
#     return area(distance(xc, yc, xp, yp))

# def is_divisible(x, y):
#     if x % y == 0:
#         return True
#     else:
#         return False

# def is_divisible(x, y):
#     return x % y == 0

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

# print(factorial(5))

def fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(7))

def factorial (n):
    if not isinstance(n, int):
        print ('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print ('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)



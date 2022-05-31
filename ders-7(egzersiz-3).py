import math
def square_root(a):
    x=0.75*a
    epsilon = 0.000001
    while True:
        y = (x + a/x) / 2
        if (abs(y-x)<epsilon):
            break
        x = y
    return x

def test_square_root(n):
    for i in range(1,n+1):
        print(i,"\t",square_root(i),"\t",math.sqrt(i),"\t",abs(square_root(i)-math.sqrt(i)))

test_square_root(9)



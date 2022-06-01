import math
def factorial(n):
    if(n==0):
        return 1
    return factorial(n-1)*n

def function_1(k):
    return (factorial(k*4)*(1103+26390*k))/(factorial(k)**4)*(396**(k*4))
    


def estimate_pi():
    epsilon = 10**(-15)
    k = -1
    t = 0
    while True:
        k = k + 1
        t =t+function_1(k)
        
        if(abs(math.pi-(1/(t*(8**(1/2))/9801)))<epsilon):
            return (1/(t*(8**(1/2))/9801))
            break

print(estimate_pi())
        





        
        



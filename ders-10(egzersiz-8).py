import random
def has_duplicates(t):
    t2 = []
    t2.extend(t)
    t2.sort()
    for i in range(len(t2)-1):
        if(t2[i]==t2[i+1]):
            return True
    return False

def random_class():
    l = []
    for i in range(23):
        l.append(random.randint(1,365))
    return l

def calculate_probability(r):
    x = 0
    y = 0
    for i in range(r):
        if(has_duplicates(random_class())==True):
            x += 1
    return x/r*100

print(calculate_probability(999999))
def middle(t):
    del(t[0],t[len(t)-1])
    return t

print(middle([1,2,3,4,5]))
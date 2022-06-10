fin = open("words.txt")
def build_list():
    res = []
    for line in fin:
        word = line.strip()
        res.append(word)
    return res

def odd_or_even(t):
    if(len(t)%2==1):
        return int((len(t)-1)/2)
    else:
        return int(len(t)/2)

def bisect(t, w):
    a = odd_or_even(t)
    if(t[a]==w):
        return True
    elif(a==0):
        return False
    if(t[a]>w):
        return bisect(t[:a], w)
    if(t[a]<w):
        return bisect(t[a+1:], w)


print(bisect(build_list(), 'car'))
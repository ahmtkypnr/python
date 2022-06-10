from re import A


def histogram(s):
    d = dict()
    for c in s:
        a = d.get(c,0)
        d[c] = a + 1
    return d

def print_hist(h):
    t = h.keys()
    a = list(h)
    a.sort()
    for c in a:
        print (c, h[c])
    

h = histogram("ahmet ikbal")
print_hist(h)

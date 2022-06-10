def histogram(s):
    d = dict()
    for c in s:
        a = d.get(c,0)
        d[c] = a + 1
    return d

print(histogram("concisely"))
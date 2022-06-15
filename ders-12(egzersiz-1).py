fin = open("words.txt")

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def most_frequent(s):
    hist = histogram(s)
    t = []
    for x, freq in hist.items():
        t.append((freq, x))
    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)
    return res

for line in fin:
    word = line.strip()
    print(most_frequent(word))
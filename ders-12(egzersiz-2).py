fin = open("words.txt")
def print_anagrams(word_list):
    d = dict()
    d2 = dict()
    d3 = dict()
    l = []
    for line in word_list:
        word = line.strip()
        t = list(word)
        t.sort()
        k = tuple(t)
        d.setdefault(k,[])
        d[k].append(word)
    for key in d:
        if(len(d[key])!=1):
            d2[key] = len(d[key])
    for key, count in d2.items():
        l.append((count, key))
    l.sort(reverse=True)
    for count, key in l:
        print(d[key])

print_anagrams(fin)
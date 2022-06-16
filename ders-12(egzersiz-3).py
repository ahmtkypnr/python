fin = open("words.txt")
def control_metathesis(w1, w2):
    a1 = enumerate(w1)
    a2 = enumerate(w2)
    tru = 0
    for t in a1:
        if(t in a2):
            tru += 1
    if(tru==len(w1)-2):
        return True
    return False

def find_metathesis_pairs(word_list):
    d = dict()
    for line in word_list:
        word = line.strip()
        t = list(word)
        t.sort()
        k = tuple(t)
        d.setdefault(k,[])
        d[k].append(word)
    for val in d.values():
        if(len(val)!=1):
            for i in range(len(val)-1):
                for k in range(i+1, len(val)):
                    if(control_metathesis(val[i], val[k])):
                        print([val[i],val[k]])

find_metathesis_pairs(fin)
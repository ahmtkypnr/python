from time import time


fin = open("words.txt")
def build_list():
    res = []
    for line in fin:
        word = line.strip()
        res.append(word)
    return res

def build_list2():
    res = []
    for line in fin:
        word = line.strip()
        res = res + [word]
    return res

build_list2()
print(time())
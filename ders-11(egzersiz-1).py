from this import d


fin = open("words.txt")
def make_dict():
    words = dict()
    for line in fin:
        word = line.strip()
        words[word] = 0
    print(words)
make_dict()

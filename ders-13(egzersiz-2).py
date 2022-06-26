import string
fin = open("words3.txt")
def edit_line(line):
    t = line.split()
    for 
def edit_file(file):
    d = dict()
    for line in file:
        t = line.split()
        for piece in t:
            word = piece.strip(string.punctuation)
            word = word.lower()
            d[word] = d.get(word, 0) + 1
    return d


print(edit_file(fin))

def count(file):
    d = dict()
    word = edit_file(file)
    d[word] = d.get(word, 0) + 1
    return d
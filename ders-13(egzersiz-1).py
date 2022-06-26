import string
fin = open("words3.txt")
def edit_file(file):
    d = dict()
    for line in file:
        t = line.split()
        for piece in t:
            word = piece.strip(string.punctuation)
            word = word.lower()
            d[word] = d.get(word, 0) + 1
    print(d)
    print(len(d))

for line in fin:
    for char in string.punctuation:
        line = line.replace(char,'')
    print (line.lower().strip())

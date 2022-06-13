fin = open("words.txt")
def make_dict():
    words = dict()
    for line in fin:
        word = line.strip()
        words[word] = 0
    return words
word_list = make_dict()

def rotate_Word(string, i):
    x = ""
    for c in string:
        a = chr(ord(c)+i)
        x = x + a
    return x

def find_rotate_pairs(word_list):
    for word in word_list:
        for i in range(1,14):
            rotated = rotate_Word(word,i)
            if(rotated in word_list):
                print(word, i, rotated)

find_rotate_pairs(word_list)
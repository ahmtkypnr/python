from pronounce import read_dictionary
fin = open("words.txt")
def make_dict():
    words = dict()
    for line in fin:
        word = line.strip()
        words[word] = 0
    return words
word_list = make_dict()

def has_duplicates(w):
    for c in w:
        if(w.count(c)>1):
            return True
    return False

def find_homophone():
    d = read_dictionary()
    for word in word_list:
        if(len(word)>2 and has_duplicates(word)==False and word in d):
            h1 = word[1:]
            h2 = word[0] + word[2:]
            if(h1 in d and h2 in d):
                if(d[word]==d[h1]==d[h2]):
                    return word

print(find_homophone())


fin = open("words2.txt")
def build_list():
    res = []
    for line in fin:
        word = line.strip()
        res.append(word)
    return res
word_list2 = build_list()

def sort_by_length(word_list):
    t = []
    res = []
    for word in word_list:
        t.append((len(word),word))
    t.sort(reverse=True)
    for length, word in t:
        res.append(word)
    return res
word_list3 = sort_by_length(word_list2)

def find_children_words(word):
    res = []
    for i in range(len(word)):
        new_word = word[:i]+word[i+1:]
        if(new_word in word_list2):
            res.append(new_word)
    return res
known = {"":True}
def is_reducable(word):
    global known
    if(word in known):
        return known[word]
    for w in find_children_words(word):
        if(is_reducable(w)==True):
            known[w] = True
            return True
        else:
            known[w] = False
    known[word] = False
    return False

def find_longest_reducable(word_list):
    for word in word_list:
        if(is_reducable(word)):
            return word

print(find_longest_reducable(word_list3))
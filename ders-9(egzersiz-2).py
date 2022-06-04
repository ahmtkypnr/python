fin = open('words.txt')

def has_no_e(word):
    for letter in word:
        if(letter=='e'):
            return False
    return True

def print_has_no_e():
    x = 0
    y = 0
    for word in fin:
        if(has_no_e(word)==True):
            print(word)
            x = x + 1
        else:
            y = y + 1
    a = x/(x+y)*100
    print(a)

print_has_no_e()
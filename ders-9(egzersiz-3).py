import string


fin = open('words.txt')
string = input()

def avoids(word):
    for letter2 in string:
        if(letter2 in word):
                return False
    return True

def print_avoids():
    x = 0
    for word in fin:
        if(avoids(word)==True):
           x = x + 1
    print(x)

print_avoids()


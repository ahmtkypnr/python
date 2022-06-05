from re import X


fin = open('words.txt')

def is_abecedarian(word):
    for i in range(len(word)-1):
        if(word[i+1]<word[i]):
            return False
    return True
x = 0
for line in fin:
    word = line.strip()
    if(is_abecedarian(word)==True):
        print(word)
        x = x + 1
print(x)

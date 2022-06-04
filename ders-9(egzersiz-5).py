def uses_all(word, string):
    for letter2 in string:
        if(letter2 not in word):
            return False
    return True

print(uses_all("ahmet ikbal", "ahmetikbls"))
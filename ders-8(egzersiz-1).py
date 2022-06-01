def write_reverse(word):
    index = 0
    while index<len(word):
        print(word[len(word)-1-index]),
        index = index+1

write_reverse("ahmet")
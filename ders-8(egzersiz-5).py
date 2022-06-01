def count(string, letter, index):
    count = 0
    for harf in string[index:]:
        if(harf==letter):
            count = count + 1
    print(count)

count("ahmet ikbal", "a", 9)
def count(string, letter):
    count = 0
    for harf in string:
        if(harf==letter):
            count = count + 1
    print(count)

count("ahmet ikbal", "a")
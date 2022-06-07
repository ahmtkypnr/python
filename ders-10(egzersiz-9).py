def remove_duplicates(t):
    d = []
    for x in t:
        if(x not in d):
            d.append(x)
    return d

print(remove_duplicates([1,2,3,4,5,1,4,6,7]))
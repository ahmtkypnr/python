def nested_sum(nlist):
    t = 0
    for list in nlist:
        for element in list:
            t += element
    return t

print(nested_sum([[54,544,21],[6,86],[3]]))
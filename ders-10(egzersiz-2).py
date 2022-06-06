def capitalize_nested(t):
    m = []
    for l in t:
        n = []
        for s in l:
            n.append(s.capitalize())
        m.append(n)
    return m

t = [["asdsd","falk"],["asffsa"]]

print(capitalize_nested(t))
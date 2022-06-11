def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[])
        inverse[val].append(key)
    return inverse

d = {"a":1,"b":2,"c":1,"d":1}
print(invert_dict(d))
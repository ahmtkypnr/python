def rotate_Word(string, i):
    x = ""
    for c in string:
        a = chr(ord(c)+i)
        x = x + a
    return x

y=rotate_Word("ahmet", 103)

print(rotate_Word(y, -103))
from re import S


def right_justify(s):
    print((70-len(s))*" " + s)
s = input()
right_justify(s)
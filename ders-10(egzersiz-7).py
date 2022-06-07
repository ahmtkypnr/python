def is_anagram(s1, s2):
    t1 = list(s1)
    t2 = list(s2)
    t1.sort()
    t2.sort()
    if(t1 == t2):
        return True
    else:
        return False

print(is_anagram("ahmet", "thmea"))

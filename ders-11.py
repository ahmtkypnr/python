# eng2sp = dict()
# eng2sp['one'] = 'uno'
# print(eng2sp)

# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp)
# print(eng2sp["one"])
# print("one" in eng2sp)
# print("uno" in eng2sp)
# vals = eng2sp.values()
# print("uno" in vals)

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d

# h = histogram('a')
# print (h)
# print(h.get('a', 0))
# print(h.get('b', 0))

# def reverse_lookup(d, v):
#     for k in d:
#         if d[k] == v:
#             return k
#     raise LookupError()     #Raise istisnayı gösteriyor!

# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse

# known = {0:0, 1:1}
# def fibonacci(n):       #Memo
#     if n in known:
#         return known[n]
#     res = fibonacci(n-1) + fibonacci(n-2)
#     known[n] = res
#     return res


# been_called = False
# def example2():
#     global been_called
#     been_called = True
# print(been_called)



# t = "a","b","c"
# t = ("a","b","c")

# t1 = "a",
# print(type(t1))

# t = tuple()

# t = tuple("ahmet")
# print(t[1:3])

# print((0, 1, 2) < (0, 3, 4))   #İlk elemandan başlayarak sırayla kıyaslıyor!

# temp = a
# a = b
# b = temp   #Değişkenlerin birbirlerinin değerlerini değiştirmesi tuple ile daha kısa
# a, b = b, a
# addr = 'monty@python.org'
# uname, domain = addr.split('@')


# def printall(*args):
#     print(args)
# printall(1, 2.0, '3')
# t = (7, 3)
# divmod(*t)


# s = 'abc'
# t = [0, 1, 2]
# zip(s, t)
# for pair in zip(s, t):
#     print(pair)
# list(zip(s, t))

# list(zip('Anne', 'Elk'))

# t = [('a', 0), ('b', 1), ('c', 2)]
# for letter, number in t:
#     print(number, letter)

# for index, element in enumerate('abc'):
#     print(index, element)


# d = {'a':0, 'b':1, 'c':2}
# t = d.items()
# print(t)

# t = [('a', 0), ('c', 2), ('b', 1)]
# d = dict(t)
# print(d)

# d = dict(zip('abc', range(3)))
# print(d)
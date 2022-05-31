x = 0
x = x+1

def countdown(n):
    while n > 0:
        print (n)
        n = n-1
    print ('Blastoff!')

def sequence(n):
    while n != 1:
        print (n),
        if n%2 == 0: # n is even
            n = n/2
        else: # n is odd
            n = n*3+1

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print (line)
# print ('Done!')

a=4
x=3
while True:
    print (x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y
#abs() mutlak değer fonksiyonu


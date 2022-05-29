def do_twice(f,a):
    f(a)
    f(a)

def print_twice(b):
    print(b)
    print(b)

do_twice(print_twice,"spam")



from functools import reduce

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(10))

def fib_1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fib_1(10))

def fib_2(n):
    f = lambda r, i: (r[1], sum(r))
    xs = range(n)
    z = (0, 1)
    r = reduce(f, xs, z)
    return r[0]

print(fib_2(10))

from functools import reduce

n = int(input('Enter a number: '))
xs = range(1, n + 1)

sp = input('Would you like the sum or the product? [S/p]')
r = reduce(lambda a, x: a * x, xs, 1) if sp.lower() == 'p' else sum(xs)

def fac(n):
    return 1 if n <= 1 else n * fac(n - 1)

def product(xs):
    return 1 if not xs else xs[0] * product(xs[1:])

def fac(n):
    return n * fac(n - 1) if n > 1 else 1

def product(xs):
    return xs[0] * product(xs[1:]) if xs else 1

print(r)

from functools import reduce

def digits(n):
    r = []
    for x in str(n):
        r.append(x)
    return r

print(digits(1234))

def digits_1(n):
    return reduce(lambda r, x: r + [x], str(n), [])

print(digits_1(1234))

def digits_2(n):
    return list(str(n))

print(digits_2(1234))

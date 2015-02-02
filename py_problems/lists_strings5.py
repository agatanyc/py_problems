def total(xs):
    r = 0
    for x in xs:
        r += x
        print(r)
    return r

xs = [1, 2, 3, 4, 5, 6]
print(total(xs))

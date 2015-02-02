def get_odd(xs):
    r = []
    for i in range(len(xs)):
        if i % 2 != 0:
            r.append(xs[i])
    return r

xs = [1, 2, 3, 4, 5, 6, 7]
print(get_odd(xs))

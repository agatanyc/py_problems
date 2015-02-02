def combine(xs, ys):
    """(list) -> list"""
    r = []
    for i in range(len(xs)):
        r.append(xs[i])
        r.append(ys[i])
    return r

xs = [1, 2, 3]
ys = ['a', 'b', 'c']
print(combine(xs, ys))

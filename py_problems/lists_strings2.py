def reverse(xs):
    """(list) -> list

    Equivalent to list(reversed(xs)).
    """
    ys = xs[:]
    ys.reverse()
    return ys

if __name__ == '__main__':
    xs = [1, 2, 3, 4]
    ys = reverse(xs)
    print(ys)

    assert(ys == [4, 3, 2, 1])

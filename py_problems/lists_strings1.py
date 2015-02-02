def the_largest(xs):
    """(list) -> int"""
    r = 0
    for x in xs:
        if x > r:
            r = x
    return r

if __name__ == '__main__':
    xs = [10, 3, 4, 15]
    print(the_largest(xs))

    assert(the_largest(xs) == 15)


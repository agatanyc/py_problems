def in_list(xs, n):
    return n in xs


if __name__ == '__main__':
    xs = [2, 5, 7, 8]
    print(in_list(xs, 5))

    assert(in_list(xs, 5) == True)
    assert(in_list(xs, 1) == False)


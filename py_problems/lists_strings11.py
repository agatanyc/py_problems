def merge(xs, ys):
    """(list, list) -> list

    Given two sorted lists, return a sorted list containing all elements of the
    original lists.  Does not modify the original lists.  Uses O(N) time and
    O(N) space, where N is the sum of the lengths of the original lists.
    """
    r = []
    i, m = 0, len(xs)
    j, n = 0, len(ys)
    while i < m and j < n:
        x = xs[i]
        y = ys[j]
        if x < y:
            r.append(x)
            i += 1
        else:
            r.append(y)
            j += 1
    r.extend(xs[i:])
    r.extend(ys[j:])
    return r

if __name__ == '__main__':
    xs = [1, 2, 10]
    ys = [8, 9, 11]
    assert([1, 2, 8, 9, 10, 11] == merge(xs, ys))


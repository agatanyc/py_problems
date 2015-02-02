def max_len(xs):
    """(list) -> int"""
    r = []
    for x in xs:
        r.append(len(x))
    return max(r)


def print_rect_2(xs, i):
    """(list, int) -> NoneType"""
    for x in xs:
        fmt = '{} {:'+ str(i) +'} {}'
        return fmt.format('*', x, '*')

def print_rect(x, i):
    """(list, int) -> NoneType"""
    fmt = '{} {:'+ str(i) +'} {}'
    return fmt.format('*', x, '*')




xs = ['agata', 'jo', 'tara']
i = max_len(xs)
for x in xs:
    print(print_rect(x, i))

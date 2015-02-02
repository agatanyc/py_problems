def max_len(xs):
    """(list) -> int"""
    r = []
    for x in xs:
        r.append(len(x))
    return max(r)

def print_rect(x, i):
    """(list, int) -> NoneType"""
    fmt = '{} {:'+ str(i) +'} {}'
    return fmt.format('*', x, '*')

xs = ['agata', 'jo', 'tara']
i = max_len(xs)
print((i + 4) * '*')
for x in xs:
    print(print_rect(x, i))
print((i + 4) * '*')

def add(cs, ds):    # takes and returns lists of digits
    a = int(''.join(cs))
    b = int(''.join(ds))
    r = a + b
    return list(str(r))

def add_1(cs, ds, base=10):
    r = []
    carry = 0
    m, n = len(cs), len(ds)
    for i in range(max(m, n)):
        c = int(cs[m - i - 1]) if i < m else 0
        d = int(ds[n - i - 1]) if i < n else 0
        s = carry + c + d
        r.append(str(s % base))
        carry = s // base
    r.reverse()
    return r

print(add([     '1', '2', '5'],
          ['4', '5', '6', '7']))

print(add_1([     '1', '2', '5'],
            ['4', '5', '6', '7']))

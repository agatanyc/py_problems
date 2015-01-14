#!/usr/bin/env python3

def is_prime(n):
    """(int) -> bool"""
    return all(n % i for i in range(2, n))

# strictly evaluated

def primes_thru_v1(n):
    """(int) -> list"""
    r = []
    for x in range(2, n + 1):
        if is_prime(x):
            r.append(x)
    return r

def primes_thru_v2(n):
    """(int) -> list"""
    return [x for x in range(2, n + 1) if is_prime(x)]

def primes_thru_v3(n):
    """(int) -> list"""
    return filter(is_prime, range(2, n + 1))

# TODO lazily evaluated

if __name__ == '__main__':
    assert(     is_prime(2) )
    assert(     is_prime(3) )
    assert( not is_prime(4) )
    assert(     is_prime(5) )
    assert( not is_prime(6) )

    for p in primes_thru(n):
        print(p)

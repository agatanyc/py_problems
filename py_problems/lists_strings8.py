def on_all(xs, f):
    for x in xs:
        f(x)

def print_square(x):
    print(x * x)

on_all(range(20), print_square)

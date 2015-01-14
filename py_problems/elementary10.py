def is_leap_year(x):
    if x % 4 == 0:
        return True
    if x % 100 == 0 and x % 400 == 0:
        return True
    return False

def leap_years(xs):
    years = []
    for x in xs:
        if is_leap_year(x):
            years.append(x)
    return years

xs = range(2016, 2037)
print(leap_years(xs))


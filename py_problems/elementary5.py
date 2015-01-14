number = int(input('Enter a number: '))
xs = range(1, number + 1)
r = 0
for x in xs:
    if x % 3 == 0 or x % 5 == 0:
        r += x
print(r)

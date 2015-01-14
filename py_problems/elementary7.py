operand1 = range(1, 13)
operand2 = range(1, 13)
s=" "*15
print(s.join([str(i) for i in operand1]))
print(190 * '-')
r = 0
for x in operand1:
    row=[]
    for y in operand2:
        r = x * y
        row.append('{:<3}{:<3}{:<3}={:>3}'.format(str(y), '*',str(x),str(r)))
        #new_row.format('left aligned')
        #row.append(str(x) +' * '+ str(y) + ' =  ' + str(r) )
    print(" | ".join(row))

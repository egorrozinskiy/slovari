A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
a = A.difference(B)
b = C.difference(D)
c = D.difference(A)
d = B.difference(C)
k = a.intersection(b)
m = c.intersection(d)
l = k.update(m)
print(k)
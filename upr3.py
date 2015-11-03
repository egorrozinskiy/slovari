input = open('input.txt' , 'r')
line = input.read()
line = line.replace('.' , ' ')
line = line.replace('!' , ' ')
line = line.replace(',' , ' ')
line = line.replace('?' , ' ')
line = line.split()
for i in line:
    i = i.lower()
A = dict()
for x in line:
    if x in A:
        A[x] += 1
    else:
        A[x] = 1        
for key in A:
    print(key, A[key])
maxx=0
for key in A:
    if A[key] > maxx:
        maxx = A[key]
        m = key
print(' макс - ', m, maxx)
        
    


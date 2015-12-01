ru_en=dict()
sl=open('input.txt')
slt=open('output.txt','w')
s=sl.readline().rstrip()
while len(s)>0:
    en,ru=list(s.split('\t-\t'))
    if ',' in ru:
        for i in ru.split(','):
            i=i.lstrip()
            if i in ru_en:
                ru_en[i]=ru_en[i]+', '+en
            else:
                ru_en[i]=en
    else:
        if ru in ru_en: 
            ru_en[ru]=ru_en[ru]+', '+en
        else:
            ru_en[ru]=en

    s=sl.readline().rstrip()

key_sort=sorted(ru_en.keys())
for i in key_sort:
    print('\t-\t'.join( (i,ru_en[i]) ),file=slt)

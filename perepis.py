with open('Perepis.txt', 'r') as f:
    a=0
    for i in f:
        b=i.split()
        if i[-5:]<'1978':
            a+=1
    print(a)
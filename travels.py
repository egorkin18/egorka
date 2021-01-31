with open('travels.txt', 'r') as f:
    a=0
    c=0
    d=0
    k=0
    for i in f:
        b=i.split()
        if i[0:1]=='1':
            a+=int(i[-4:])

        if i[0:1]=='2':
            c+=int(i[-4:])

        if i[0:1]=='3':
            d+=int(i[-4:])

        if i[10:15]=='Липки':
            k+=int(i[-4:])



    print('Первое октября: ',a)
    print('Второе октября: ',c)
    print('Третье октября: ',d)

    if (a>c) and (a>d):
        print('Самое большое количество за 1 октября, ',a)
    elif (c>a) and (c>d):
        print('Самое большое количество за 2 октября, ',c)
    elif (d>a) and (d>c):
        print('Самое большое количество за 3 октября, ',d)

    print('Масса грузов из Липок: ',k)






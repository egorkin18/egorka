with open('Perepis.txt', 'r') as f:
    a=int(input('Введите первое число диапазона(большее): '))
    b=int(input('Введите второе число диапазона: '))
    k=0
    for i in f:
        c=i.split()
        if a<=int(i[-5:])<=b:
            k+=1
            print(i[::1])
    print(k)


with open('mat_dv.txt','r') as f:
    k1=0
    k2=0
    k3=0
    k4=0
    max=0
    for i in f:
        a=i.split()
        print(a)

        if a[2]=='8':
            k1=int(a[3])+int(a[4])

        if a[2]=='9':
            k2=a[3]+a[4]

        if a[2]=='10':
            k3=a[3]+a[4]

        if a[2]=='11':
            k4=int(a[3]+a[4])



    print('8 классы: ',k1)
    print('9 классы: ',k2)
    print('10 классы: ',k3)
    print('11 классы: ',k4)





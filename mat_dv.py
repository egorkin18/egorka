from random import randint
l=list()
for i in range(0,10):
    l.append(randint(1,15))
    while l.count(l[i])>0:
        l[i]=randint(1,15)
print(l)



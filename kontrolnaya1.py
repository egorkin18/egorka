a=0
s=0

def decorator(uskorenie):
    def wrapper(a,v0,v1,t):
        uskorenie(a,v0,v1,t)
        s=(v0*t)+((a*t*t)/(2))
        print('Путь: ',s,' км.')
    return wrapper

def uskorenie(a,v0,v1,t):
    a=(v1-v0)/t
    print('Ускорение: ',a)

try:
    v0=int(input('Введите начальную скорость: '))
    v1=int(input('Введите конечную скорость: '))
    t=int(input('Введите время: '))
    uskorenie=decorator(uskorenie)
    uskorenie(a,v0,v1,t)
except ZeroDivisionError:
    print('Введите правильное время')
except ValueError:
    print('Введите правильный тип данных')
else:
    print('Всё гуд')





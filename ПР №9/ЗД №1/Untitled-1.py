from random import randint
def f ():
    stroka1 = [randint(0,5) for i in range(3)]
    stroka2 = [randint(0,5) for i in range(3)]
    stroka3 = [randint(0,5) for i in range(3)]
    print(stroka1)
    print(stroka2)
    print(stroka3)
    print()
    print(sorted(stroka1))
    print(sorted(stroka2))
    print(sorted(stroka3))
f()

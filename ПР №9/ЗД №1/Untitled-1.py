from random import randint
def f():
    M=randint(1,3)
    N=randint(1,3)
    a = [[randint(0, 9) for _ in range(M)] for _ in range(N)]
    for i in a:
        print(*i)
    for i in a: 
        print(*sorted(i))
f()

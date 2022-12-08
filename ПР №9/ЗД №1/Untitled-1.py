from random import randint
def f():
    N = 3
    M = 3
    a = [[randint(0, 9) for _ in range(M)] for _ in range(N)]
    for i in a:
        print(i)
    for i in a:
        print(sorted(i))
f()

def f():
    from random import randint 
    m=randint(1,3)
    n=randint(1,3)

    a = [[randint(1, 9) for i in range(m)] for j in range(n)]
    for i in a :
        print(*i)
    print()
    for r in a :
        r = (list((1 if min(r) % 2 else 0) if j == min(r) else j for j in r))

        print(*r)
f()

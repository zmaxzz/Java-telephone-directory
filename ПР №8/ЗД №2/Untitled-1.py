def F(n):
    m=[]
    for x in range(1,n+1):
        if n % x ==0:
            a=m.append(x)
            print(m[-1], end=' ')
F(10)
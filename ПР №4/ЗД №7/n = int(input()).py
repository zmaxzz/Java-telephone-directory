def F(n):         
    N = 1
    sum = 0
    for i in range(1, n + 1):
        N *= i
        sum += N
    print(sum)
F(4)
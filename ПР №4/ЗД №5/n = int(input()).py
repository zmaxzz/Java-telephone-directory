def F(n):
    sum = 0                   
    for x in range(1, n + 1):
        sum += x ** 3
    print(sum)
F(4)
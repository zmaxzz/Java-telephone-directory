def F(x,y):
    i = 1
    while y > x:
        x += 0.1*x
        i += 1
    print(i)
F(8,20)
    
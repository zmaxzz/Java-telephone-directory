def F(a, b, c):                              
    if a == b == c:
        return 3
    if a == b or b==c or c==a:
        return 2
    else:
        return 0
print(F(1, 1, 7))
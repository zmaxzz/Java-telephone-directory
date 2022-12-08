def F():
    x=int(input())
    if x == 0:
        return x
    return max([x,F()])
print(F())
def F():
    n = int(input())
    i = int(input())
    r = 0
    while i != 0:
        if i == n:
            r += 1
        n = i
        i = int(input())    
    print(r)
F()
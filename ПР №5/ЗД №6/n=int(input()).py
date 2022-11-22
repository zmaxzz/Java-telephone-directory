def F():
    n = int(input())
    i = 0
    r = 0
    l = 0
    while n != 0:
        i += 1
        r += n
        n = int(input())
        l = r // i
    print(l)
F()
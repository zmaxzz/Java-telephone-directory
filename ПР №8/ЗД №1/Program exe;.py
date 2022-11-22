def F():
    a=150
    b=25
    c=200
    d=100
    h=a//b
    z=c//d
    while h != z:
        if h > z:
            h = h - z
        else:
            z = z - h
    print(h)
F()        
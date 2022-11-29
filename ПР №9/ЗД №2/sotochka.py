from random import randint
def f():
    n = 3
    m = 3
    ch = 0
    nch = 1
    a=[randint(0,9) for i in range(3)]
    b=[randint(0,9) for i in range(3)]
    c=[randint(0,9) for i in range(3)]
        
    print(a[0],a[1],a[2])
    print(b[0],b[1],b[2])
    print(c[0],c[1],c[2])
    print()
    print()
    #####
    if a[0]>a[1]>a[2]:
        min = a[2]
        if min % 2 ==1:
            min = 1
            print(a[0],a[1],min)
        else:
            min = 0
            print(a[0],a[1],min)
            
                
    elif a[0]<a[1]<a[2]:
        min = a[0]
        if min % 2 ==1:
            min = 1
            print(min,a[1],a[2])
        else:
            min = 0
            print(min,a[1],a[2])
    else:
        min = a[1]
        if min % 2 ==1:
            min = 1
            print(a[0],min,a[2])
        else:
            min = 0
            print(a[0],min,a[2])

    if b[0]>b[1]>b[2]:
        min = b[2]
        if min % 2 ==1:
            min = 1
            print(b[0],b[1],min)
        else:
            min = 0
            print(b[0],b[1],min)
            
    elif b[0]<b[1]<b[2]:
        min = b[0]
        if min % 2 ==1:
            min = 1
            print(min,b[1],b[2])
        else:
            min = 0
            print(min,b[1],b[2])
            
    else:
        min = b[1]
        if min % 2 ==1:
            min = 1
            print(b[0],min,b[2])
        else:
            min = 0
            print(b[0],min,b[2])

    if c[0]>c[1]>c[2]:
        min = c[2]
        if min % 2 ==1:
            min = 1
            print(c[0],c[1],min)
        else:
            min = 0
            print(c[0],c[1],min)
            
    elif c[0]<c[1]<c[2]:
        min = c[0]
        if min % 2 ==1:
            min = 1
            print(min,c[1],c[2])
        else:
            min = 0
            print(min,c[1],c[2])
            
    else:
        min = c[1]
        if min % 2 ==1:
            min = 1
            print(c[0],min,c[2])
        else:
            min = 0
            print(c[0],min,c[2])
f()


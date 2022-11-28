def f():
    n = 3
    m = 3
    ch = 0
    nch = 1
    a = []
    for i in range(n):
        b = []
        for j in range(3):
            print('Введите [',i,',',j,'] элемент')
            b.append(int(input()))
        a.append(b)
        
    print(a[0][0],a[0][1],a[0][2])
    print(a[1][0],a[1][1],a[1][2])
    print(a[2][0],a[2][1],a[2][2])
    print()
    print()
    #####
    if a[0][0]>a[0][1]>a[0][2]:
        min = a[0][2]
        if min % 2 ==1:
            min = 1
            print(a[0][0],a[0][1],min)
        else:
            min = 0
            print(a[0][0],a[0][1],min)
            
                
    elif a[0][0]<a[0][1]<a[0][2]:
        min = a[0][0]
        if min % 2 ==1:
            min = 1
            print(min,a[0][1],a[0][2])
        else:
            min = 0
            print(min,a[0][1],a[0][2])
    else:
        min = a[0][1]
        if min % 2 ==1:
            min = 1
            print(a[0][0],min,a[0][2])
        else:
            min = 0
            print(a[0][0],min,a[0][2])

    if a[1][0]>a[1][1]>a[1][2]:
        min = a[1][2]
        if min % 2 ==1:
            min = 1
            print(a[1][0],a[1][1],min)
        else:
            min = 0
            print(a[1][0],a[1][1],min)
            
    elif a[1][0]<a[1][1]<a[1][2]:
        min = a[1][0]
        if min % 2 ==1:
            min = 1
            print(min,a[1][1],a[1][2])
        else:
            min = 0
            print(min,a[1][1],a[1][2])
            
    else:
        min = a[1][1]
        if min % 2 ==1:
            min = 1
            print(a[1][0],min,a[1][2])
        else:
            min = 0
            print(a[1][0],min,a[1][2])

    if a[2][0]>a[2][1]>a[2][2]:
        min = a[2][2]
        if min % 2 ==1:
            min = 1
            print(a[2][0],a[2][1],min)
        else:
            min = 0
            print(a[2][0],a[2][1],min)
            
    elif a[2][0]<a[2][1]<a[2][2]:
        min = a[2][0]
        if min % 2 ==1:
            min = 1
            print(min,a[2][1],a[2][2])
        else:
            min = 0
            print(min,a[2][1],a[2][2])
            
    else:
        min = a[2][1]
        if min % 2 ==1:
            min = 1
            print(a[2][0],min,a[2][2])
        else:
            min = 0
            print(a[2][0],min,a[2][2])
f()
        


F=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vvod2.txt')
L=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vvod2.txt')
S=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vivod2.txt','w+')
Q=F.readlines()
N=L.readlines(5)
R=L.readlines(5)
I=L.readlines(5)
M=[int(x) for x in Q]
a=[int(x) for x in N]
b=[int(x) for x in R]
c=[int(x) for x in I]
def f():
    n = 3
    m = 3
    ch = 0
    nch = 1
    S.write(str(a[0]))
    S.write(str(a[1]))
    S.write(str(a[2]))
    S.write(str(b[0]))
    S.write(str(b[1]))
    S.write(str(b[2]))
    S.write(str(c[0]))
    S.write(str(c[1]))
    S.write(str(c[2]))
    S.write('\n')
    S.write('\n')
    #####
    if a[0]>a[1]>a[2]:
        min = a[2]
        if min % 2 ==1:
            min = 1
            S.write(str(a[0]))
            S.write(str(a[1]))
            S.write(str(min))
        else:
            min = 0
            S.write(str(a[0]))
            S.write(str(a[1]))
            S.write(str(min))

            
                
    elif a[0]<a[1]<a[2]:
        min = a[0]
        if min % 2 ==1:
            min = 1
            S.write(str(min))
            S.write(str(a[1]))
            S.write(str(a[2]))
        else:
            min = 0
            S.write(str(min))
            S.write(str(a[1]))
            S.write(str(a[2]))
    else:
        min = a[1]
        if min % 2 ==1:
            min = 1
            S.write(str(a[0]))
            S.write(str(min))
            S.write(str(a[2]))
        else:
            min = 0
            S.write(str(a[0]))
            S.write(str(min))
            S.write(str(a[2]))

    if b[0]>b[1]>b[2]:
        min = b[2]
        if min % 2 ==1:
            min = 1
            S.write(str(b[0]))
            S.write(str(b[1]))
            S.write(str(min))
        else:
            min = 0
            S.write(str(b[0]))
            S.write(str(b[1]))
            S.write(str(min))
            
    elif b[0]<b[1]<b[2]:
        min = b[0]
        if min % 2 ==1:
            min = 1
            S.write(str(min))
            S.write(str(b[1]))
            S.write(str(b[2]))
        else:
            min = 0
            S.write(str(min))
            S.write(str(b[1]))
            S.write(str(b[2]))
            
    else:
        min = b[1]
        if min % 2 ==1:
            min = 1
            S.write(str(b[0]))
            S.write(str(min))
            S.write(str(b[2]))
        else:
            min = 0
            S.write(str(b[0]))
            S.write(str(min))
            S.write(str(b[2]))

    if c[0]>c[1]>c[2]:
        min = c[2]
        if min % 2 ==1:
            min = 1
            S.write(str(c[0]))
            S.write(str(c[1]))
            S.write(str(min))
        else:
            min = 0
            S.write(str(c[0]))
            S.write(str(c[1]))
            S.write(str(min))
            
    elif c[0]<c[1]<c[2]:
        min = c[0]
        if min % 2 ==1:
            min = 1
            S.write(str(min))
            S.write(str(c[1]))
            S.write(str(c[2]))
        else:
            min = 0
            S.write(str(min))
            S.write(str(c[1]))
            S.write(str(c[2]))
            
    else:
        min = c[1]
        if min % 2 ==1:
            min = 1
            S.write(str(c[0]))
            S.write(str(min))
            S.write(str(c[2]))
        else:
            min = 0
            S.write(str(c[0]))
            S.write(str(min))
            S.write(str(c[2]))
f()
S.close()

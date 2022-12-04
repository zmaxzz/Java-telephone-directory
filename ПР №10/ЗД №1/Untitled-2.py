F=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vvod1.txt')
L=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vvod1.txt')
S=open(r'C:\\Users\user\\Desktop\\Bubnov-M.M_Y-224_vivod1.txt','w+')
Q=F.readlines()
N=L.readlines(7)
R=L.readlines(5)
I=L.readlines(5)
M=[int(x) for x in N]
A=[int(x) for x in R]
P=[int(x) for x in Q]
T=[int(x) for x in I]
def f ():
    print(A)
    print(P)
    print(T)
    print()
    S.write(str(sorted(A)))
    S.write(str(sorted(P)))
    S.write(str(sorted(T)))
f()
S.close()
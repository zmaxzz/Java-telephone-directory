F=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vvod2.txt')
L=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vvod2.txt')
S=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vivod2.txt','w+')
Q=F.readlines()
N=L.readlines(7)
R=L.readlines(5)
I=L.readlines(5)
M=[int(x) for x in N]
A=[int(x) for x in R]
P=[int(x) for x in Q]
T=[int(x) for x in I]
def f():
    a = [i for i in P]
    S.write(str(a))
    S.write(str(list((1 if min(a) % 2 else 0) if j == min(a) else j for j in a)))

f()
S.close()

F=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vvod2.txt')
S=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vivod2.txt','w+')
Q=F.readlines()
P=[int(x) for x in Q]
def f():
    a = [i for i in P]
    S.write(str(a))
    S.write(str(list((1 if min(a) % 2 else 0) if j == min(a) else j for j in a)))

f()
S.close()

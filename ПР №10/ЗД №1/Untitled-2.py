F=open(r'C:\\Users\\user\\Desktop\\Bubnov-M.M_Y-224_vvod1.txt')
S=open(r'C:\\Users\user\\Desktop\\Bubnov-M.M_Y-224_vivod1.txt','w+')
Q=F.readlines()
P=[int(x) for x in Q]
def f ():
    a = [i for i in P]
    S.write(str(a))
    S.write(str(sorted(a)))

f()
S.close()

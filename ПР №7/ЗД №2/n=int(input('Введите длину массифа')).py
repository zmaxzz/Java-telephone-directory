n=int(input('Введите длину массифа'))
s=[]
a=[]
for x in range(n):
    s.append(int(input()))
print('исходный массиф')
for x in s:
    if x not in a:
        a.append(x)
print(a)
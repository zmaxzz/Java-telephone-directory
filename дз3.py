"# -- coding: utf-8 --"
задание №1
def add(x,y,z):                          
    return x+y+z
print(add(3,5,8))

задание №2
def F(a,b):
    return 1/2 * a*b
print(F(7,4))

задание №3
def F(n):
    hours = n % (60 * 24) // 60
    minutes = n % 60
    print(hours, ":", minutes)
print(F(280000))

задание №4
def F(a, b, l, n):
    return a + (2*n*a) + (2*b*n) + l
print(F(8,4 , 7, 3))

задание№5
   if x > y and z > y:
        print(b)
    if y > x and z > x:
        print(a)
    if y > z and x > z:
        print(z)
print(F(1,9,-2))

задание №6
def F(a,b,c,d): 
    if a % 2 == 0 and b % 2 == 0:
        if c % 2 == 0 and d % 2 == 0:
            print('Да')
    if a % 2 == 1 and b % 2 == 1:
        if c % 2 == 1 and d % 2 == 1:
            print('Да')
    if a % 2 == 0 and b % 2 == 0:
        if c % 2 == 1 and d % 2 == 1:
            print('Да')
    if a % 2 == 1 and b % 2 == 1:
        if c % 2 == 0 and d % 2 == 0:
            print('Да')
    if a % 2 == 0 and b % 2 ==1:
        if c % 2 == 0 and d % 2 == 0:
            print('Нет')
    if a % 2 == 1 and b % 2 ==0:
        if c % 2 == 0 and d % 2 == 0:
            print('Нет')
    if a % 2 == 0 and b % 2 ==0:
        if c % 2 == 1 and d % 2 == 0:
            print('Нет')
    if a % 2 == 0 and b % 2 ==0:
        if c % 2 == 0 and d % 2 == 1:
            print('Нет')
    if a % 2 == 1 and b % 2 ==0:
        if c % 2 == 1 and d % 2 == 1:
            print('Нет')
    if a % 2 == 0 and b % 2 ==1:
        if c % 2 == 1 and d % 2 == 1:
            print('Нет')
    if a % 2 == 1 and b % 2 ==1:
        if c % 2 == 0 and d % 2 == 1:
            print('Нет')
    if a % 2 == 1 and b % 2 ==1:
        if c % 2 == 1 and d % 2 == 0:
            print('Нет')
    if a % 2 == 1 and b % 2 == 0:
        if c % 2 == 1 and d % 2 == 0:
            print('Да')
    if a % 2 == 0 and b % 2 == 1:
        if c % 2 == 0 and d % 2 == 1:
            print('Да')
    if a % 2 == 1 and b % 2 == 0:
        if c % 2 == 0 and d % 2 == 1:
            print('Да')
    if a % 2 == 0 and b % 2 == 1:
        if c % 2 == 1 and d % 2 == 0:
            print('Да')
print(F(4,3,8,6))

задание №7
def F(x):
    if x%4==0 and x%100!=0 and x%400!=0:
        print("Да")
    else:
        print("Нет")
print(F(2004))

задание №8
def F(a, b, c):                              
    if a == b == c:
        return 3
    if a == b or b==c or c==a:
        return 2
    else:
        return 0
print(F(1, 1, 7))

задание №9
def F(n,m,k):
    if m*n//k:
        print("Да")
    else:
        print("Нет")
print(F(1,5,7))

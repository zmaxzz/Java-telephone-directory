"# -- coding: utf-8 --"
def F(x,y,z)
return x+y+z
print(F(1,2,3))
def F(a,b): #2#
return 1/2 * a*b
print(F(7,6))
def F(n): 
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, ":", minutes)
print(F(280000))
def F(a, b, l, n): 
return a + (2*n*a) + (2*b*n) + l
print(F(8,4 , 7, 3))
def F(x, y, z): #5#
if x > y and z > y:
print(y)
if y > x and z > x:
print(x)
if y > z and x > z:
print(z)
print(F(3,4,-2))
def F(a,b,c,d): #6#
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
def F(x): #7#
if x//4==0 and x//100!=0 and x//400!=0:
print("Да")
else:
print("Нет")
print(F(2004))
def F(x, y, z): #8#
if x == y == z:
return 3
if x == y or y==z or z==x:
return 2
else:
return 0
print(F(6, 24, 93))
def F(n,m,k): #9#
if m*n//k:
print("Да")
else:
print("Нет")
print(F(1,5,7))

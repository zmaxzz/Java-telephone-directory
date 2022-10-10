a=int(input())
b=int(input())
while a<=b:
    print(a)
    a=a+1
a=int(input())
b=int(input())
while a<b:
    a=a+1
    print(a)
while a>b:
    a=a-1
    print(a)
a=int(input())
b=int(input())
while a>b:
    a=a-1
    if a%2==1:
        print(a)
n=int(input())
sum=0
for x in range(n):
    y=int(input())
    sum+=y
    print(sum)
n=int(input())
sum=0
for x in range(1,n+1):
    sum += x**3
print(sum)
n=int(input())
y=1
for x in range(1,n+1):
    y *= x
print(y)
n=int(input())
y=1
for x in range(1,n+1):
    y *= x
    sum += y
print(sum)
n=int(input())
for x in range(1,n+1):
    for y in range(1,x+1):
        print(y, end ='')
    print()
n=int(input())
def F(n):
   if n==1 or n==2:
       return 1
   else:
       return F(n-2)+ F(n-1)
print(F(n+2)-1)
n=int(input())
def f(n):
   if n==1 or n==2:
       return 1
   else:
       return f(n-2)+ f(n-1)
print(f(n+2)-1)
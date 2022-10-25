n = int(input())          
i = 1
sum = 0
for x in range(1, n + 1):
    i *= x
    sum += i
print(sum)
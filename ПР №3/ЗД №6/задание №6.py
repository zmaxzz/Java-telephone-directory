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
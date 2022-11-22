def F(n):
    s = []
    for x in range(n):
        print('введите элемент')
        s.append(int(input()))
    print('исходный массиф')
    for x in range(n):
        if s[x] < 0 and s[x + 1] < 0:
            print('Пара:', s[x], s[x + 1])
    print()
F(10) 
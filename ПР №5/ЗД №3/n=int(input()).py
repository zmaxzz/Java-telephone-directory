def F(n):
        i = 2
        r = 1
        while i < n+1:
                i *= 2
                r += 1  
        print(r - 1, i // 2)
F(8)            
    
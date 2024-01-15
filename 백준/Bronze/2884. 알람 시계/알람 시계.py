h, m = map(int, input().split())

if h == 0:
    h = (60*24 + m -45) // 60
else:
    h = (60*h + m -45) // 60
    
m = (60*h + m -45) % 60

if h == 24:
    print('0',m)
    
else : print(h,m)
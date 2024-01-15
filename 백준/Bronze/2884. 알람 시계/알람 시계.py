h, m = map(int, input().split())

if m >= 45 :
    m = m - 45
    
else :
    m = 60 + m - 45
    if h == 0 :
        h = 24 - 1
    else : 
        h = h -1
    
print (h,m)
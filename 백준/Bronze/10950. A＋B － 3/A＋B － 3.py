t = int(input())

list = []

for i in range(1,t+1):
    a,b = map(int,input().split())
    list.append(a+b)
    
for value in list:
    print(value)
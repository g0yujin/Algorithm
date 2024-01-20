import sys

T = int(sys.stdin.readline())
list = []

for i in range(1, T+1):
    a, b = map(int,sys.stdin.readline().split())
    list.append(a+b)

for i in list:
    print(i)
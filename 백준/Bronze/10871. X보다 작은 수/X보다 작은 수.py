import sys

N, X = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))

def smaller(num):
    if num < X:
        return num
    else:
        return

result = filter(smaller, A)
print(*result)
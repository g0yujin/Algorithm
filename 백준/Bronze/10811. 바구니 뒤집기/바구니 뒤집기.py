import sys

N, M = map(int, sys.stdin.readline().split())

basket = []
for x in range(1, N+1):
    basket.append(x)

temp = 0
for x in range(M):
    i, j = map(int, sys.stdin.readline().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

print(*basket)
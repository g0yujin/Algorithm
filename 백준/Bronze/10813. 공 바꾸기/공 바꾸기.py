import sys

N, M = map(int, sys.stdin.readline().split())

bucket = []
for a in range(1, N+1):
    bucket.append(a)


for a in range(M):
    i, j = map(int, sys.stdin.readline().split())
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]


print(*bucket)
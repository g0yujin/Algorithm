import sys

N, M = map(int, input().split())

bucket = []

for i in range(N):
    bucket.append(0)

for i in range(M):
    I, J, K = map(int, sys.stdin.readline().split())
    ball = []
    for i in range(J-I+1):
        ball.append(K)

    bucket[I - 1:J ] = ball

print(*bucket)
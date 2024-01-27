import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
M = max(score)

avg =[]

for i in score:
    avg.append(i / M * 100)

print(sum(avg) / N)
import sys

chess = list(map(int, sys.stdin.readline().split()))

chess[0] = 1 - chess[0]
chess[1] = 1 - chess[1]
chess[2] = 2 - chess[2]
chess[3] = 2 - chess[3]
chess[4] = 2 - chess[4]
chess[5] = 8 - chess[5]

print(*chess)
import sys

T = int(sys.stdin.readline().rstrip())


result = []

for i in range(T):
    N, W = sys.stdin.readline().split()
    N = int(N)
    W = list(W)
    repeat = []

    for i in range(0, len(W)):
        repeat.append(W[i]*N)

    result.append(''.join(repeat))

print(*result, sep='\n')

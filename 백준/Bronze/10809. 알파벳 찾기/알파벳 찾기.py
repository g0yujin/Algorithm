import sys
from string import ascii_lowercase

S = list(sys.stdin.readline().rstrip())

result = []

for i in ascii_lowercase:
    if i in S:
        result.append(S.index(i))
    else:
        result.append(-1)

print(*result)

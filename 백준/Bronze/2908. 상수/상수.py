import sys

A, B = map(str, sys.stdin.readline().split())

reverse = []
reverse.append(A[::-1])
reverse.append(B[::-1])

print(max(reverse))
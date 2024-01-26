import sys

remainder = []

for i in range(10):
    n = int(sys.stdin.readline())
    remainder.append(n % 42)

print(len(set(remainder)))
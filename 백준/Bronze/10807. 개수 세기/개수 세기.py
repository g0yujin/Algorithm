import sys

N = int(input())

numbers = list(map(int, sys.stdin.readline().split()))

v = int(input())

print(numbers.count(v))
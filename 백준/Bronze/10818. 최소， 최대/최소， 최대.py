import sys

N = int(input())

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

print(numbers[0],numbers[N-1])
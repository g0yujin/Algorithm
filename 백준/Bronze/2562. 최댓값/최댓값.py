import sys

numbers =[]

for i in range(9):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers_sorted = sorted(numbers)
a = numbers_sorted[8]

print(a, numbers.index(a)+1, sep = '\n')
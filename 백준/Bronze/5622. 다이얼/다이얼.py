import sys

word = list(map(str, sys.stdin.readline().rstrip()))

time = []

for i in word:
    if i == 'A' or i == 'B' or i == 'C':
        time.append(3)
    elif i == 'D' or i == 'E' or i == 'F':
        time.append(4)
    elif i == 'G' or i == 'H' or i == 'I':
        time.append(5)
    elif i == 'J' or i == 'K' or i == 'L':
        time.append(6)
    elif i == 'M' or i == 'N' or i == 'O':
        time.append(7)
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        time.append(8)
    elif i == 'T' or i == 'U' or i == 'V':
        time.append(9)
    elif i == 'W' or i == 'X' or i == 'Y' or i =='Z':
        time.append(10)

print(sum(time))
import sys

student = []
for i in range(1, 31):
    student.append(i)


for i in range(28):
    n = int(sys.stdin.readline())
    student.remove(n)
    
print(f'{min(student)}\n{max(student)}')
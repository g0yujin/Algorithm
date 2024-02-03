import sys

credit = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5,
          'D0': 1.0 , 'F': 0.0}
n = 20
sum = 0
sum_1 = 0
for i in range(n):
    obj, score, grade = sys.stdin.readline().split()
    if grade == 'P':
        pass
    else:
        sum += float(score) * credit[grade]
        sum_1 += float(score)

print(format(sum/sum_1, ".6f"))
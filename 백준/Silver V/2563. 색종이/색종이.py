import sys

canvas = [[0] * 100 for _ in range(100)]

num = int(sys.stdin.readline())

def print_array(array, row, col):
    for i in range(row):
        for j in range(col):
            print(array[i][j], end=' ')
        print()

def change_array(array, row_s, row_e, col_s, col_e):
    for k in range(row_s, row_e):
        for l in range(col_s, col_e):
            if array[k][l] == 0:
                array[k][l] = array[k][l] + 1


def get_stack_area(array, row, col):
    count = 0 
    for m in range(row):
        for n in range(col):
            if array[m][n] == 1:
                count += 1
    print(count)


for i in range(num):
    x, y = map(int,sys.stdin.readline().split())
    change_array(canvas, y, y+10, x, x+10)

get_stack_area(canvas, 100, 100)
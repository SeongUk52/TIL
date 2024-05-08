import sys
input = sys.stdin.readline


def cal(num):
    if num == 1:
        cal1()
    elif num == 2:
        cal2()
    elif num == 3:
        cal3()
    elif num == 4:
        cal4()
    elif num == 5:
        cal5()
    elif num == 6:
        cal6()


def cal1():
    global mat
    temp = [[]for _ in range(len(mat))]
    for i in range(len(mat)):
        temp[n - i - 1] = mat[i]
    mat = temp


def cal2():
    global mat
    temp = [list(reversed(mat[i])) for i in range(len(mat))]
    mat = temp


def cal3():
    global mat
    temp = [[] for i in range(len(mat[0]))]
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            temp[i].append(mat[len(mat) - j - 1][i])
    mat = temp


def cal4():
    global mat
    temp = [[] for i in range(len(mat[0]))]
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            temp[i].append(mat[j][len(mat[0]) - i - 1])
    mat = temp


def cal5():
    global mat
    lenRow = len(mat)
    lenCol = len(mat[0])
    mat1 = mat[:lenRow//2]
    mat2 = [0] * (lenRow//2)
    mat3 = mat[lenRow//2:]
    mat4 = [0] * (lenRow//2)
    for i in range(lenRow // 2):
        mat2[i] = mat1[i][lenCol//2:]
        mat1[i] = mat1[i][:lenCol//2]
        mat4[i] = mat3[i][:lenCol//2]
        mat3[i] = mat3[i][lenCol//2:]
    temp = []
    for i in range(lenRow//2):
        temp.append(mat4[i][:] + mat1[i][:])
    for i in range(lenRow//2):
        temp.append(mat3[i][:] + mat2[i][:])
    mat = temp


def cal6():

    global mat
    lenRow = len(mat)
    lenCol = len(mat[0])
    mat1 = mat[:lenRow//2]
    mat2 = [0] * (lenRow//2)
    mat3 = mat[lenRow//2:]
    mat4 = [0] * (lenRow//2)
    for i in range(lenRow // 2):
        mat2[i] = mat1[i][lenCol//2:]
        mat1[i] = mat1[i][:lenCol//2]
        mat4[i] = mat3[i][:lenCol//2]
        mat3[i] = mat3[i][lenCol//2:]
    temp = []
    for i in range(lenRow//2):
        temp.append(mat2[i][:] + mat3[i][:])
    for i in range(lenRow//2):
        temp.append(mat1[i][:] + mat4[i][:])
    mat = temp


n, m, r = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
coms = list(map(int, input().split()))
k = 0
while k < len(coms) - 1:
    if coms[k] == coms[k + 1] == 1 or coms[k] == coms[k + 1] == 2:
        coms.pop(k)
        coms.pop(k)
    k += 1
k = 0
while k < len(coms) - 3:
    if coms[k] == coms[k + 1] == coms[k + 2] == coms[k + 3]:
        for i in range(4):
            coms.pop(k)
    k += 1

for i in coms:
    cal(i)

for i in mat:
    print(*i)

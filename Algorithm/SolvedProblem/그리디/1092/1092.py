import sys
input = sys.stdin.readline

n = int(input())
arrN = list(map(int, input().split()))
arrN.sort(reverse=True)
m = int(input())
arrM = list(map(int, input().split()))
arrM.sort(reverse=True)
cnt = 0

while arrM:
    cnt += 1
    flag = True
    for i in range(n):
        if not arrM:
            break

        for j in arrM:
            if arrN[i] >= j:
                arrM.remove(j)
                flag = False
                break
    if flag:
        cnt = -1
        arrM = []
        break

print(cnt)

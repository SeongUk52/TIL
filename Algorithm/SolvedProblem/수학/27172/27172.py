import sys
input = sys.stdin.readline

n = int(input())
ll = list(map(int, input().split()))
score = [0] * n
mn = max(ll)
siv = [-1] * (mn + 1)

for i in range(n):
    siv[ll[i]] = i

for i in range(n):
    num = ll[i]
    if num > mn // 2:
        continue
    for j in range(num + num, mn + 1, num):
        if siv[j] != -1:
            score[i] += 1
            score[siv[j]] -= 1

print(*score)

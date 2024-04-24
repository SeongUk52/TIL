import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]
arr.sort()
maxi = 0
result = 0

for i in range(m):
    egg = min(m - i, n)

    if result < arr[i] * egg:
        result = arr[i] * egg
        maxi = arr[i]

print(maxi, result)

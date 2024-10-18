import sys

input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
if n == 1:
    if data[0] > m:
        print(0)
    else:
        print(data[0])
else:
    temp = 0
    ans = 0
    l, r = 0, 1
    temp += data[l]
    while l <= r < n:
        if data[r] <= m - temp:
            temp += data[r]
            r += 1
        else:
            if l == r:
                l += 1
                r += 1
                temp = 0
                continue
            temp -= data[l]
            l += 1
        ans = max(ans, temp)
    print(ans)

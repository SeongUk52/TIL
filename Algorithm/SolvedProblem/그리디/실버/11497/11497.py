import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    maxi = max(0, arr[0] - arr[1])
    for i in range((n + 1)//2 - 1):
        maxi = max(maxi, arr[2 * i] - arr[2 * i + 2])
    for i in range(n//2 - 1):
        maxi = max(maxi, arr[2 * i + 1] - arr[2 * i + 3])
    print(maxi)

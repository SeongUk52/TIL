import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
result = 0
for i in range(1, n + 1):
    result += abs(i - arr[i - 1])
print(result)

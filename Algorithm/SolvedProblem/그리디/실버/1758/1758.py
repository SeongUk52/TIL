import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
result = 0
for i in range(n):
    result += max(0, arr[i] - i)
print(result)

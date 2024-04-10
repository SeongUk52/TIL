import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

for i in range(n):
    arr[i] += i

print(max(arr) + 2)

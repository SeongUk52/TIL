import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
print(sum([arr[i] for i in range(n) if i % 3 != 2]))

import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
site = {}
for _ in range(n):
    s, p = input().rstrip().split()
    site[s] = p

for _ in range(m):
    print(site[input().rstrip()])

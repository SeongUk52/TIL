import sys
input = sys.stdin.readline

def find(n):
    if par[n] != n:
        par[n] = find(par[n])
    return par[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        par[b] = a
        num[a] += num[b]
        num[b] += num[a]
    print(num[a])


def setter(n):
    if n not in par:
        par[n] = n
        num[n] = 1


for _ in range(int(input())):
    f = int(input())
    par, num = {}, {}
    for _ in range(f):
        a, b = input().split()
        setter(a)
        setter(b)
        union(a, b)

import sys
input = sys.stdin.readline


def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        arr[b] = a
        setSize[a] += setSize[b]
        setSize[b] = 0
    elif b < a:
        arr[a] = b
        setSize[b] += setSize[a]
        setSize[a] = 0


n = int(input())
arr = [i for i in range(10 ** 6 + 1)]
setSize = [1 for i in range(10 ** 6 + 1)]

for _ in range(n):
    commands = list(input().split())
    if commands[0] == 'I':
        union(int(commands[1]), int(commands[2]))
    if commands[0] == 'Q':
        print(setSize[find(int(commands[1]))])

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


n, m = map(int, input().split())
sizeArr = [0] + list(map(int, input().split()))
rainArr = [0] + list(map(int, input().split()))
arr = [i for i in range(n + 1)]
countArr = [1] * (n + 1)
result = 0


def find(n):
    if arr[n] != n:
        arr[n] = find(arr[n])
    return arr[n]


def union(a, b):
    global result
    a, b = find(a), find(b)
    if a == b:
        return

    if a > b:
        a, b = b, a

    if sizeArr[a] < rainArr[a]:
        result -= countArr[a]

    if sizeArr[b] < rainArr[b]:
        result -= countArr[b]

    arr[b] = a
    sizeArr[a] += sizeArr[b]
    rainArr[a] += rainArr[b]
    countArr[a] += countArr[b]

    if sizeArr[a] < rainArr[a]:
        result += countArr[a]


for i in range(1, n + 1):
    if sizeArr[i] < rainArr[i]:
        result += 1


for _ in range(m):
    inputL = list(map(int, input().split()))
    if inputL[0] == 2:
        print(result)

    if inputL[0] == 1:
        union(inputL[1], inputL[2])

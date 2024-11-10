import sys

input = sys.stdin.readline


def func(index):
    global origin

    if index >= len(origin): return 0
    if cache[index] != -1: return cache[index]

    cache[index] = func(index + 1) + 1

    for recode in r:
        key = recode[0]
        value = recode[1]

        if origin[index:index + len(key)] == key:
            cache[index] = max(cache[index], func(index + len(key)) + value)

    return cache[index]


origin = input()[:-1]
m = int(input())
cache = [-1 for _ in range(len(origin) + 1)]
r = []

for _ in range(m):
    r.append(list(map(str, input().split())))
    r[-1][1] = int(r[-1][1])

print(func(0))

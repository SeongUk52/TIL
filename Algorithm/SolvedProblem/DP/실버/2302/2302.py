import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

seats, idx = list(), 0
for _ in range(M):
    vip = int(input())
    seats.append(vip - idx - 1)
    idx = vip
seats.append(N - idx)

F = {1: 1, 2: 1}


def fibonacci(n):
    if n in F:
        return F[n]
    F[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return F[n]


answer = 1
for seat in seats:
    if seat > 1:
        answer *= fibonacci(seat + 1)

print(answer)

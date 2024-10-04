import sys

fibonacci = [0, 1, 1] + ([0] * 9998)

before_2 = 1
before_1 = 1
current = before_2 + before_1

for i in range(3, 10000 + 1):
    fibonacci[i] = current

    before_2 = before_1
    before_1 = current
    current = before_2 + before_1

T = int(sys.stdin.readline())

for j in range(1, T + 1):
    P, Q = map(int, sys.stdin.readline().split())

    remain = fibonacci[P] % Q

    print(f'Case #{j}: {remain}')

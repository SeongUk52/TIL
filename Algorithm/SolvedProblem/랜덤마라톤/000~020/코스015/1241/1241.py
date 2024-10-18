import sys

N = int(sys.stdin.readline())

circle, result = [0] * N, [0] * N
for i in range(N):
    circle[i] = int(sys.stdin.readline())

matrix = [0 for _ in range(max(circle) + 1)]
for c in circle:
    matrix[c] += 1

for n in range(N):
    k = 1
    while k * k <= circle[n]:
        if circle[n] % k == 0:
            if k * k != circle[n]:
                result[n] += matrix[k] + matrix[circle[n] // k]
            else:
                result[n] += matrix[k]
        k += 1

answer = ""
for r in result:
    answer += str(r - 1) + "\n"
print(answer)

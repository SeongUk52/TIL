a, b = map(int, input().split())
mini = min(a, b)

for i in range(1, mini + 1):
    if a % i != 0 or b % i != 0:
        continue
    print(i, a // i, b // i)

n, t = map(int, input().split())
result = -1
for _ in range(n):
    S, I, C = map(int, input().split())
    for _ in range(C):
        if S >= t:
            if result == -1:
                result = S - t
                break
            else:
                result = min(S - t, result)
        S += I
print(result)

def facto(n):
    if n > 1:
        return facto(n - 1) * n
    else:
        return 1

n = int(input())
num = facto(n)
cnt = 0
while num % 10 == 0:
    num //= 10
    cnt += 1

print(cnt)
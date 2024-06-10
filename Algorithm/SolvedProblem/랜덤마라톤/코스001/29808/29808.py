cnt = 0
s = int(input())
result = []
if s % 4763 == 0:
    s //= 4763
    for i in range(401):
        for j in range(401):
            if i < 200:
                r1 = i
                a = i * 508
            else:
                r1 = i - 200
                a = r1 * 108
            if j < 200:
                r2 = j
                b = j * 212
            else:
                r2 = j - 200
                b = r2 * 305
            if s == a + b and [r1, r2] not in result:
                result.append([r1, r2])
                cnt += 1
print(cnt)
for i in result:
    print(*i)

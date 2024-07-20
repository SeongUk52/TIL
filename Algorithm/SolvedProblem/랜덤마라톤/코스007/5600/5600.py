a, b, c = map(int, input().split())
ll = [2] * (a + b + c + 1)
later = []
for _ in range(int(input())):
    i, j, k, r = map(int, input().split())
    if r == 1:
        ll[i] = 1
        ll[j] = 1
        ll[k] = 1
    else:
        later.append((i, j, k))

for n in later:
    i, j, k = n
    indexes = [i, j, k]
    l = [ll[i], ll[j], ll[k]]
    if l.count(1) == 2:
        ll[indexes[l.index(2)]] = 0

for i in ll[1:]:
    print(i)

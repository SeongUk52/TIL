n = int(input())
ll = [i for i in range(1, 10)]

for i in range(1, n + 1):
    nl = ll[:]
    for j in ll:
        for k in range(1, 10):
            num = j * k
            if num in nl:
                continue
            if num >= 10 ** i:
                break
            nl.append(num)
    ll = nl[:]

print(len(ll))

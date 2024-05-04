n = int(input())
alpha = {}
va = []
init = []
result = 0

for i in range(n):
    ll = list(input())

    if not ll[0] in init:
        init.append(ll[0])

    for i in range(len(ll)):
        if not ll[i] in alpha:
            alpha[ll[i]] = 0
        alpha[ll[i]] += 10 ** (len(ll) - i - 1)

for i in alpha.values():
    va.append(i)

va.sort()

if len(alpha) >= 10:
    flag = False
    for i in range(len(va)):
        for j in [k for k, v in alpha.items() if v == va[i]]:
            if j not in init:
                va.remove(va[i])
                flag = True
                break

        if flag:
            break

for i in range(9, 0, -1):
    if not va:
        break
    result += i * va.pop()

print(result)

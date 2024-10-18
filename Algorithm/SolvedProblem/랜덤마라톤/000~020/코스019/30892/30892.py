n, k, t = map(int, input().split())
sharks = list(map(int, input().split()))

sharks.sort()
sharks.append(float('inf'))
stack = []
for i in range(n):
    if k == 0:
        break
    elif sharks[i] >= t:
        while stack and sharks[i] >= t and k != 0:
            t += stack.pop()
            k -= 1
        if k != 0 and sharks[i] < t:
            t += sharks[i]
            k -= 1
        else:
            break
    elif sharks[i + 1] < t:
        stack.append(sharks[i])
    else:
        t += sharks[i]
        k -= 1

while k > 0 and stack:
    t += stack.pop()
    k -= 1

print(t)

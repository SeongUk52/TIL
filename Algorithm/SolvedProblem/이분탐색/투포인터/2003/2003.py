n, m = map(int, input().split())
ll = list(map(int, input().split()))

left = 0
right = 0
cnt = 0
suma = ll[0]

while left < n:

    if suma == m:
        cnt += 1
        right += 1
        if right >= n:
            break
        suma += ll[right]
        continue

    if suma < m:
        right += 1
        if right >= n:
            break
        suma += ll[right]
        continue

    if suma > m:
        suma -= ll[left]
        left += 1
        continue

print(cnt)

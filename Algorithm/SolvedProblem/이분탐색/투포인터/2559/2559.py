n, k = map(int, input().split())
ll = list(map(int, input().split()))

result = sum(ll[:k])
suma = result

for i in range(n - k):
    suma += ll[i + k]
    suma -= ll[i]
    if suma > result:
        result = suma

print(result)

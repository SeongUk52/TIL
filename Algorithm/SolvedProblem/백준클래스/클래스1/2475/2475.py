ll = list(map(int, input().split()))
result = 0
for i in ll:
    result += i * i
result %= 10
print(result)

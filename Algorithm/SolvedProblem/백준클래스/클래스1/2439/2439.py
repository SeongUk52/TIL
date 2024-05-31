n = int(input())
result = [" " * (n - i) + "*" * i for i in range(1, n + 1)]
for i in result:
    print(i)

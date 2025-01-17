n = int(input())
data = sorted(int(input()) for _ in range(n))

result = sorted(int(str(i) + str(j)) for i in data[:4] for j in data[:4] if i != j)
print(result[2])
n = int(input())
result = 0
for i in range(n + 1):
    temp = i
    for j in str(i):
        temp += int(j)

    if temp == n:
        result = i
        break
print(result)
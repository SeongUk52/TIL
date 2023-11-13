n = int(input())
result = 0

for i in range(1, n + 1):
    if i < 100:
        result += 1

    elif int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
        result += 1

print(result)

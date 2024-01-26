n = int(input())

death = [0 for _ in range(21)]
num = [0 for _ in range(21)]
num[1] = 1
death[4] = 1

for i in range(2, 21):
    birth = num[i - 1]
    num[i] = num[i - 1] * 2 - death[i]

    if i % 2 == 0:
        if i + 4 <= 20:
            death[i + 4] += birth
    else:
        if i + 3 <= 20:
            death[i + 3] += birth
print(num[n])
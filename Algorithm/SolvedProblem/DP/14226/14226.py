s = int(input())
time = list(range(1003))

for i in range(2, s + 1):
    j = 2
    while i * j <= 1002:
        time[i * j] = min(time[i * j], time[i] + j)
        time[i * j - 1] = min(time[i * j - 1], time[i * j] + 1)
        j += 1

print(time[s])
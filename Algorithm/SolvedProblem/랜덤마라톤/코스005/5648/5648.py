results = []
inputs = list(map(list, input().split()))
n = int(''.join(inputs[0]))
results += inputs[1:]
while len(results) < n:
    results += list(map(list, input().split()))

for i in range(n):
    results[i].reverse()
    results[i] = int(''.join(results[i]))

results.sort()
print(*results, sep="\n")

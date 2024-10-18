N, K = map(int, input().split())

tables = [int(x) for x in input().split()]

arr_NS = []
arr_SN = []

for i in range(1, N): # N-S
    arr_NS.append(tables[i - 1] - tables[i] - K)

for i in range(1, N): # S-N
    arr_SN.append(tables[i] - tables[i - 1] - K)

temp_NS = [0] * (N - 1)
temp_NS[0] = arr_NS[0]
for i in range(1, N - 1):
    temp_NS[i] = max(0, temp_NS[i - 1]) + arr_NS[i]

temp_SN = [0] * (N - 1)
temp_SN[0] = arr_SN[0]
for i in range(1, N - 1):
    temp_SN[i] = max(0, temp_SN[i - 1]) + arr_SN[i]

print(max((max(temp_NS),max(temp_SN))))

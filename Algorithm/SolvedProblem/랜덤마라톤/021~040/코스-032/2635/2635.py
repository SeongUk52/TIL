n = int(input())
max_list = []

for i in range(1, n + 1):
    seq = [n, i]
    while seq[-2] >= seq[-1]:
        seq.append(seq[-2] - seq[-1])
    if len(seq) > len(max_list):
        max_list = seq

print(len(max_list))
print(*max_list)
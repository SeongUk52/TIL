from itertools import permutations

a = [int(x) for _ in range(3) for x in input().split()]
res = float('inf')

for perm in permutations(range(1, 10)):
    if all(
        sum(perm[i:i+3]) == sum(perm[:3]) for i in range(0, 9, 3)  # Rows
    ) and all(
        sum(perm[i::3]) == sum(perm[:3]) for i in range(3)          # Columns
    ) and sum(perm[0::4]) == sum(perm[:3]) and sum(perm[2:8:2]) == sum(perm[:3]):  # Diagonals
        res = min(res, sum(abs(a[i] - perm[i]) for i in range(9)))

print(res)
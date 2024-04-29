n, k = map(int, input().split())
arr = list(map(int, input().split()))
gaps = [0] * (n - 1)

for i in range(n - 1):
    gaps[i] = arr[i + 1] - arr[i]

gaps.sort()

for i in range(k - 1):
    gaps.pop()

print(sum(gaps))

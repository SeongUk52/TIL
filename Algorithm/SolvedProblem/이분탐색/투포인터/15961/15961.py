import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.extend(arr)
left = 0
right = 0
dict_ = defaultdict(int)
result = 0

dict_[c] += 1

while right < k:
    dict_[arr[right]] += 1
    right += 1

while right < len(arr):
    result = max(result, len(dict_))
    dict_[arr[left]] -= 1
    if dict_[arr[left]] == 0:
        del dict_[arr[left]]
    dict_[arr[right]] += 1
    left += 1
    right += 1

print(result)

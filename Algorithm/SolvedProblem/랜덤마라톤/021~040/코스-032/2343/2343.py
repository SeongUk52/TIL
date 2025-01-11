N, M = map(int, input().split())
arr = list(map(int, input().split()))

left, right = max(arr), sum(arr)
while left <= right:
    mid = (left + right) // 2
    count, total = 1, 0

    for num in arr:
        if total + num > mid:
            count += 1
            total = 0
        total += num

    if count > M:
        left = mid + 1
    else:
        right = mid - 1

print(left)
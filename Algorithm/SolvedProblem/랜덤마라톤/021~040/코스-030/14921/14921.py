N = int(input())
arr = list(map(int, input().split()))
left, right, ans = 0, N - 1, float('inf')

while left < right:
    tmp = arr[left] + arr[right]
    if abs(tmp) < abs(ans):
        ans = tmp
    if tmp < 0:
        left += 1
    else:
        right -= 1

print(ans)
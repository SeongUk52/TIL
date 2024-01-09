n = int(input())
arr = list(map(int, input().split()))

arr.sort()

maxi = 2_000_000_001

result = [maxi, arr[0], arr[-1]]

left = 0
right = n - 1

while left < right:
    temp = arr[left] + arr[right]

    if result[0] > abs(temp):
        result = [abs(temp), arr[left], arr[right]]

    if temp == 0:
        break

    if temp < 0:
        left += 1

    if temp > 0:
        right -= 1

print(result[1], result[2])
import sys

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 0
sum = 0
min_length = sys.maxsize

while True:
    if sum >= S:
        min_length = min(min_length, right - left)
        sum -= numbers[left]
        left += 1
    elif right == N:
        break
    else:
        sum += numbers[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)

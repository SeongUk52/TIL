import sys

input = sys.stdin.readline

_ = input()
nums = list(map(int, input().split()))
def binary_search(lis_arr, num):
    low = -1
    high = len(lis_arr)
    while low + 1 < high:
        mid = (low + high) // 2

        if num > lis_arr[mid]:
            low = mid
        else:
            high = mid

    return high


lis_arr = [-float('infinity')]
lis_total = [(-float('infinity'), 0)]

nums = nums[::-1]

while nums:
    num = nums.pop()

    if num > lis_arr[-1]:
        lis_total.append((num, len(lis_arr)))
        lis_arr.append(num)

    else:
        idx = binary_search(lis_arr, num)
        lis_arr[idx] = num
        lis_total.append((num, idx))

lis_length = len(lis_arr) - 1
lis = []


while lis_total and lis_length:
    num, idx = lis_total.pop()
    if idx == lis_length:
        lis.append(num)
        lis_length -= 1

print(len(lis))
print(*lis[::-1])
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def length_of_lis(nums):
    if not nums:
        return 0

    lis = [nums[0]]

    for num in nums[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            idx = binary_search(lis, num)
            lis[idx] = num

    return len(lis)

n = int(input())
nums = list(map(int,input().split()))
result = length_of_lis(nums)
print(result)

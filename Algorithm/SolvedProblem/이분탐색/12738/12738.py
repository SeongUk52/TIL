def bs(arr, target):
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


def len_lis(arr):
    if not arr:
        return 0

    lis = [arr[0]]

    for i in arr[1:]:
        if i > lis[-1]:
            lis.append(i)
        else:
            idx = bs(lis, i)
            lis[idx] = i

    return len(lis)


n = int(input())
a = list(map(int, input().split()))
print(len_lis(a))

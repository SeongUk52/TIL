n = int(input())
nums = list(map(int, input().split()))

prefix_sum = 0
res = 0
for i in range(len(nums) - 1, 0, -1):
    prefix_sum += nums[i]
    res += nums[i - 1] * prefix_sum

print(res)# 동전 뒤집기
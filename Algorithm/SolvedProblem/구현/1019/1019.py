n = int(input())
nums = [0] * 10
num = 1
while n > 0:
    while n % 10 != 9:
        for i in str(n):
            nums[int(i)] += num
        n -= 1
    if n < 10:
        for i in range(n + 1):
            nums[i] += num
    else:
        for i in range(10):
            nums[i] += (n // 10 + 1) * num
    nums[0] -= num
    num *= 10
    n //= 10
print(*nums)

n = int(input())
prev1 = 1
prev2 = 1
ans = 1
for i in range(n - 2):
    ans = (prev1 + prev2) % 1_000_000_007
    prev2 = prev1
    prev1 = ans
print(ans, n - 2)

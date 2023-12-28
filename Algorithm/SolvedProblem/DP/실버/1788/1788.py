n = int(input())

sign = 0

result = 0

temp1 = 0
temp2 = 1

if n >= 2:
    for i in range(2, n + 1):
        result = (temp1 + temp2)
        temp1 = temp2
        temp2 = result
elif n <= - 2:
    for i in range(2, abs(n) + 1):
        result = (temp1 - temp2)
        temp1 = temp2
        temp2 = result
elif n != 0:
    result = 1

if result < 0:
    sign = -1
elif result > 0:
    sign = 1

print(sign)
print(abs(result)% 1000000000)
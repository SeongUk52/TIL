import sys
input = sys.stdin.readline

weights = [100, 50, 20, 10, 5, 2, 1]

n = int(input())
p = list(map(int, input().split()))
left, right = p[0], p[1]

for i in range(2, n):
    if left == right:
        left += p[i]
    elif left < right:
        left += p[i]
    else:
        right += p[i]

difference = abs(left - right)

if difference == 0:
    print(0)
else:
    count = 0
    for weight in weights:
        if difference // weight != 0:
            count += difference // weight
            difference %= weight
    print(count)
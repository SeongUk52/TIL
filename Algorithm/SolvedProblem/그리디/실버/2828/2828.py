import sys
n, m = map(int, sys.stdin.readline().split())
j = int(sys.stdin.readline())
now = 1
apples = [int(sys.stdin.readline()) for _ in range(j)]
answer = 0
for apple in apples:
    if now <= apple <= now + (m - 1):
        pass
    elif now > apple:
        answer += abs(apple - now)
        now = apple
    else:
        answer += apple - (m - 1) - now
        now = apple - (m - 1)
print(answer)

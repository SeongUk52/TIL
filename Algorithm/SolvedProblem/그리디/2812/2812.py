import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().rstrip()))
stack = []
for i in nums:
    while k > 0 and stack and stack[-1] < i:
        stack.pop()
        k -= 1
    stack.append(i)

print(*stack[:len(stack) - k], sep="")

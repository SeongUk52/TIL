k = int(input())
stack = []
for _ in range(k):
    n = int(input())
    if n != 0:
        stack.append(n)
    if n == 0:
        stack.pop()

print(sum(stack))
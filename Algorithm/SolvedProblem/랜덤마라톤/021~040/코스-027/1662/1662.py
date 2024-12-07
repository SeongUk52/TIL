from sys import stdin

input = stdin.readline().strip()

def solv():
    stack, cnt, before = [], 0, 0
    for c in input:
        if c == '(':
            stack.append((cnt - 1, before))
            cnt = 0
        elif c == ')':
            cnt = cnt * stack[-1][1] + stack.pop()[0]
        else:
            cnt, before = cnt + 1, int(c)
    print(cnt)

solv()
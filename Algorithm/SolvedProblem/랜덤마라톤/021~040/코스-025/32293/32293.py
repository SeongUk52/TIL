import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
MAX_N = 5 * 10**5 + 5

for _ in range(t):
    n = int(input())
    chars = list(input().strip())
    n = len(chars)

    prev = [-1] * n
    next = [-1] * n
    for i in range(n):
        if i > 0:
            prev[i] = i - 1
        if i < n - 1:
            next[i] = i + 1

    queue = deque()
    in_queue = [False] * n
    for i in range(n):
        if chars[i] == 'A':
            queue.append(i)
            in_queue[i] = True

    while queue:
        i = queue.popleft()
        in_queue[i] = False
        if chars[i] != 'A' or next[i] == -1 or next[next[i]] == -1:
            continue
        j, k = next[i], next[next[i]]
        if chars[j] == 'B' and chars[k] == 'B':
            chars[i] = 'B'
            chars[j] = 'A'
            next[j] = next[k]
            if next[k] != -1:
                prev[next[k]] = j
            for idx in [prev[prev[i]] if prev[i] != -1 else -1, prev[i], i, j, next[j]]:
                if idx != -1 and chars[idx] == 'A' and not in_queue[idx]:
                    queue.append(idx)
                    in_queue[idx] = True

    result = []
    idx = 0
    while prev[idx] != -1:
        idx = prev[idx]
    while idx != -1:
        result.append(chars[idx])
        idx = next[idx]
    print(''.join(result))
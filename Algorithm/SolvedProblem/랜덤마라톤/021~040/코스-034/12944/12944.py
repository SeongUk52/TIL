from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def search(depth, bit_mask, value):
    global result
    if visited[bit_mask]:
        return
    visited[bit_mask] = True
    if depth % 2 == 1:
        result += n // value
    else:
        result -= n // value
    if bit_mask == full_mask or value > n:
        return
    for i in range(k):
        if bit_mask & (1 << i):
            continue
        search(depth + 1, bit_mask | (1 << i), lcm(value, cards[i]))

n, k = map(int, input().split())
cards = list(map(int, input().split()))
full_mask = (1 << k) - 1
visited = [False] * (full_mask + 1)
result = 0

for i in range(k):
    search(1, 1 << i, cards[i])

print(result)
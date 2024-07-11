t, m, n = map(int, input().split())
ll = []
for _ in range(t):
    inputs = list(input().split())
    for i in range(1, len(inputs) - 1):
        ll.append([inputs[0], int(inputs[i])])

ll.sort(key=lambda x: x[1])
index = 0
if not m > ll[-1][1]:
    while ll[index][1] < m:
        index += 1
n -= 1
while n > 0:
    n -= 1
    index += 1
    if index >= len(ll):
        index = 0

print(ll[index][0])

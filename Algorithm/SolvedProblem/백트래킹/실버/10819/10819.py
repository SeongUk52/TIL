def bt(comb):
    if len(comb) == n:
        global result
        x = 0
        for i in range(n - 1):
            x += abs(comb[i] - comb[i + 1])

        if x > result:
            result = x
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        comb.append(arr[i])
        bt(comb)
        comb.pop()
        visited[i] = False


n = int(input())

arr = list(map(int, input().split()))
result = 0
visited = [False] * n
bt([])

print(result)
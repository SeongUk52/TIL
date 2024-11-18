INF = float('inf')
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

dp = [[None for _ in range(1 << n)] for _ in range(n)]

def search(node, chk):
    if chk == (1 << n) - 1:
        if mat[node][0] != 0:
            return mat[node][0]
        else:
            return INF

    if dp[node][chk] is not None:
        return dp[node][chk]

    min_value = INF
    for i in range(1, n):
        if mat[node][i] != 0 and (chk & (1 << i)) == 0:
            min_value = min(min_value, search(i, chk | (1 << i)) + mat[node][i])

    dp[node][chk] = min_value
    return min_value

answer = search(0, 1)
print(answer)

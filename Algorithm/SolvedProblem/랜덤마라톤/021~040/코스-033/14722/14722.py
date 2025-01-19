import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, -1] for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        left_score, left_state = dp[i][j - 1]
        up_score, up_state = dp[i - 1][j]
        current = mat[i - 1][j - 1]

        left_check = (left_state + 1) % 3 == current
        up_check = (up_state + 1) % 3 == current

        if left_score + left_check > up_score + up_check:
            dp[i][j] = [left_score + left_check, current if left_check else left_state]
        else:
            dp[i][j] = [up_score + up_check, current if up_check else up_state]

print(dp[N][N][0])
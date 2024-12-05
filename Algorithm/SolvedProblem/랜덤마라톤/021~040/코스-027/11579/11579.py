def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))

    ans = 0
    for r in range(N):
        C = X[r]
        if C < 0:
            print(0)
            return
        for c in range(r, N):
            X[c] -= C * A[r][c]
        ans += C
        if ans > 2000000000:
            print(0)
            return
    print(1, ans)

T = int(input())
for _ in range(T):
    solve()
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k, t = map(int, input().split())
cnt = [0] * (n + 1)
v = []
dp = [[-1] * (k + 1) for _ in range(301)]  # -1로 초기화하여 메모이제이션 확인

# 구간 입력 및 cnt 배열 계산
for _ in range(m):
    a, b = map(int, input().split())
    for i in range(a, b):
        cnt[i] = min(t, cnt[i] + 1)

# 구간 압축
temp = cnt[1]
_count = 1
for i in range(2, n + 1):
    if cnt[i] != temp:
        v.append((_count, temp))
        _count = 1
        temp = cnt[i]
    else:
        _count += 1
v.append((_count, temp))

# DP 함수 정의
def go(here, num, prev):
    if here == len(v):
        return 0
    if dp[here][num] != -1:
        return dp[here][num]

    cost = max(0, t - v[here][1])
    real_cost = 0 if prev >= cost else cost

    if num - real_cost >= 0:
        dp[here][num] = max(
            go(here + 1, num - real_cost, cost) + v[here][0],
            go(here + 1, num, 0)
        )
    else:
        dp[here][num] = go(here + 1, num, 0)

    return dp[here][num]

# 결과 출력
print(go(0, k, 0))
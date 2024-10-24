import sys

N, m = map(int, sys.stdin.readline().rstrip().split())

act_1 = N
act_2 = N // 2
act_3 = (N + 1) // 2
act_4 = (N - 1) // 3 + 1

cnt = 1

if act_1 <= m: cnt += 1
if N > 1 and act_2 <= m: cnt += 1
if N > 1 and act_3 <= m: cnt += 1
if N > 2 and act_4 <= m: cnt += 1
if N >= 3 and act_1 + act_4 <= m: cnt += 1
if N >= 3 and act_2 + act_4 <= m: cnt += 1
if N >= 3 and act_3 + act_4 <= m: cnt += 1

print(cnt)

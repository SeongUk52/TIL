import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

# 누적합 계산
prefix_sum = [0]
for num in data:
    prefix_sum.append(prefix_sum[-1] + num)

# 누적합과 K*i의 차이를 계산
diff_count = {}
result = 0
for i in range(N + 1):
    diff = prefix_sum[i] - K * i
    if diff in diff_count:
        result += diff_count[diff]
        diff_count[diff] += 1
    else:
        diff_count[diff] = 1

print(result)
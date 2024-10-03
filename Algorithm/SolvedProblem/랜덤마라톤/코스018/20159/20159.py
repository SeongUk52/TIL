N = int(input())
arr = list(map(int, input().split()))

junghun_origin_sum = 0
for i in range(N):
    if i % 2 == 0:
        junghun_origin_sum += arr[i]
ans = junghun_origin_sum
junghun_sum = junghun_origin_sum

for i in range(N-1, 0, -2):
    junghun_sum += arr[i]
    junghun_sum -= arr[i-1]
    ans = max(ans, junghun_sum)


junghun_sum = junghun_origin_sum
for i in range(N-2, 1, -2):
    junghun_sum -= arr[i]
    junghun_sum += arr[i-1]
    ans = max(ans, junghun_sum)

print(ans)

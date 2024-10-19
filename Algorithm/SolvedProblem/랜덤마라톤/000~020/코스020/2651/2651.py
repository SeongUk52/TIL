B = int(input())
N = int(input())
dis_data = list(map(int, input().split()))
time = list(map(int, input().split()))

distance = [0] * (N + 2)
for idx, i in enumerate(dis_data):
    distance[idx + 1] = distance[idx] + i

time = [0] + time + [0]
min_time = [float('infinity')] * (N + 2)
min_time[0] = 0
cnt = [0] * (N + 2)
place = [[] for _ in range(N + 2)]

for i in range(1, N + 2):
    for j in range(i - 1, -1, -1):
        if distance[i] - distance[j] <= B and min_time[i] > min_time[j] + time[i]:
            min_time[i] = min_time[j] + time[i]
            cnt[i] = cnt[j] + 1
            place[i] = place[j] + [str(i)]

print(min_time[-1])
print(cnt[-1] - 1)
print(" ".join([str(i) for i in place[-1][:-1]]))

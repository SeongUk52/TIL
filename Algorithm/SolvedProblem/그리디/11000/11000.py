import heapq
import sys
input = sys.stdin.readline

n = int(input())
st = [list(map(int, input().split())) for _ in range(n)]
st.sort(key=lambda x: x[0])
hq = [0]

for i in range(n):
    ft = heapq.heappop(hq)
    heapq.heappush(hq, st[i][1])
    if st[i][0] < ft:
        heapq.heappush(hq, ft)

print(len(hq))

import heapq
import sys

min_heap = []  # 최소 힙
max_heap = []  # 최대 힙

N = int(input())

for _ in range(N):
    num = int(sys.stdin.readline().strip())

    # 최소 힙과 최대 힙에 번갈아가며 원소를 추가
    if len(min_heap) == len(max_heap):
        # 최대 힙에 원소 추가
        heapq.heappush(max_heap, (-num, num))
    else:
        # 최소 힙에 원소 추가
        heapq.heappush(min_heap, (num, num))

    # 최소 힙의 최솟값과 최대 힙의 최댓값을 비교하여 조건에 맞게 바꿔줌
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-min_value, min_value))
        heapq.heappush(min_heap, (max_value, max_value))

    # 중간값 출력
    print(max_heap[0][1])

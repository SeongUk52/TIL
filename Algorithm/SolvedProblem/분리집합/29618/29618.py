N, Q = map(int, input().split())

# 초기에 모든 칸은 색상이 지정되지 않은 상태로 초기화
colors = [0] * N

# 색상을 갱신할 구간 정보를 저장하는 리스트
queries = []

# 쿼리 정보를 입력받아 구간 정보로 변환하여 저장
for _ in range(Q):
    a, b, x = map(int, input().split())
    # 시작 인덱스를 0부터로 맞추기 위해 -1 처리
    queries.append((a - 1, b - 1, x))

# 각 쿼리를 처리하면서 색상을 갱신
for query in queries:
    a, b, x = query
    # 해당 구간의 모든 칸에 대해 색상을 갱신
    for i in range(a, b + 1):
        # 색상이 이미 지정된 경우는 건너뜀
        if colors[i] == 0:
            colors[i] = x

# 결과 출력
print(*colors)

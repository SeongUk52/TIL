def make_crossword(A, B):
    # 교차점 찾기
    cross_idx_a = cross_idx_b = -1
    for i, char_a in enumerate(A):
        if char_a in B:
            cross_idx_a = i
            cross_idx_b = B.index(char_a)
            break

    if cross_idx_a == -1 or cross_idx_b == -1:
        print("교차점을 찾을 수 없습니다.")
        return

    N, M = len(A), len(B)
    result = [['.' for _ in range(N)] for _ in range(M)]

    for i in range(N):
        result[cross_idx_b][i] = A[i]

    for j in range(M):
        result[j][cross_idx_a] = B[j]

    for row in result:
        print("".join(row))


A, B = input().split()
make_crossword(A, B)

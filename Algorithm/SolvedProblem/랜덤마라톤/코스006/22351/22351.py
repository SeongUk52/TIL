def solution(N):
    length = len(N)
    A_lst = [int(N[0]), int(N[:2]), int(N[:3])]
    for A in A_lst:
        B = A
        new_num = ''

        while len(new_num) < length:
            new_num += str(B)
            if new_num == N:
                return A, B

            B += 1

    return N, N


N = input()
print(*solution(N))
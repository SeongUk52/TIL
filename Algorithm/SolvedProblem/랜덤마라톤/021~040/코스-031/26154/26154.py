LIMIT = 1002
score = [[0] * 3 for _ in range(LIMIT)]

def move(N, M):
    move_cnt = M if M <= N else N + (M % N)

    for _ in range(move_cnt):
        first_move_idx = 0
        move_idx = 2

        if score[0][0] > score[0][1]:
            first_move_idx = 1

        for j in range(1, N):
            if score[j][0] > score[j][1]:
                score[j - 1][move_idx] = score[j][0]
                move_idx = 0
            else:
                score[j - 1][move_idx] = score[j][1]
                move_idx = 1

        score[N - 1][move_idx] = score[0][first_move_idx]
        score[0][first_move_idx] = score[0][2]

# Input reading
N, M = map(int, input().split())
for i in range(N):
    score[i][0], score[i][1] = map(int, input().split())

# Perform the move operation
move(N, M)

# Output the result
for i in range(N):
    if score[i][0] < score[i][1]:
        print(score[i][0], score[i][1])
    else:
        print(score[i][1], score[i][0])
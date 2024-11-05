def row_check(r, c, num):
    for x in range(9):
        if c != x and num == sdoku[r][x]:
            return False
    return True


def col_check(r, c, num):
    for x in range(9):
        if r != x and num == sdoku[x][c]:
            return False
    return True


def three_check(r, c, num):
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if r != nr + x and c != nc + y and sdoku[nr + x][nc + y] == num:
                return False
    return True


def dfs(depth, r, c, num):
    if depth > 0:
        if not row_check(r, c, num):
            return
        if not col_check(r, c, num):
            return
        if not three_check(r, c, num):
            return

    if depth >= len(zero_p):
        for k in range(9):
            print(''.join(map(str, sdoku[k])))
        exit()

    nr, nc = zero_p[depth]
    for j in range(1, 9 + 1):
        sdoku[nr][nc] = j
        dfs(depth + 1, nr, nc, j)
        sdoku[nr][nc] = 0


sdoku = []
zero_p = []
for i in range(9):
    temp = list(map(int, input()))
    for j in range(len(temp)):
        if temp[j] == 0:
            zero_p.append((i, j))
    sdoku.append(temp)

dfs(0, 0, 0, 0)

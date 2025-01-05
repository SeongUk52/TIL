# Direction vectors
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
T_Dir = [0, 2, 4, 6]
F_Dir = [1, 3, 5, 7]


# Fireball class to represent each fireball
class Fireball:
    def __init__(self, x, y, massive, speed, direction):
        self.x = x
        self.y = y
        self.massive = massive
        self.speed = speed
        self.direction = direction


# Input variables
N, M, K = 0, 0, 0
MAP = [[[] for _ in range(55)] for _ in range(55)]
fireballs = []


# Input function
def input_data():
    global N, M, K
    N, M, K = map(int, input().split())
    for _ in range(M):
        r, c, m, s, d = map(int, input().split())
        fireball = Fireball(r, c, m, s, d)
        fireballs.append(fireball)
        MAP[r][c].append(fireball)


# Move fireballs
def move_fireballs():
    global MAP
    # Clear the map
    MAP = [[[] for _ in range(55)] for _ in range(55)]

    for fireball in fireballs:
        move = fireball.speed % N
        nx = (fireball.x + dx[fireball.direction] * move - 1) % N + 1
        ny = (fireball.y + dy[fireball.direction] * move - 1) % N + 1
        MAP[nx][ny].append(Fireball(nx, ny, fireball.massive, fireball.speed, fireball.direction))
        fireball.x, fireball.y = nx, ny


# Sum and split fireballs
def sum_fireballs():
    global fireballs
    new_fireballs = []

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if len(MAP[i][j]) == 0:
                continue

            if len(MAP[i][j]) == 1:
                new_fireballs.append(MAP[i][j][0])
                continue

            massive_sum = sum(f.massive for f in MAP[i][j])
            speed_sum = sum(f.speed for f in MAP[i][j])
            count = len(MAP[i][j])

            even = all(f.direction % 2 == 0 for f in MAP[i][j])
            odd = all(f.direction % 2 == 1 for f in MAP[i][j])

            new_massive = massive_sum // 5
            new_speed = speed_sum // count

            if new_massive == 0:
                continue

            if even or odd:
                directions = T_Dir
            else:
                directions = F_Dir

            for direction in directions:
                new_fireballs.append(Fireball(i, j, new_massive, new_speed, direction))

    fireballs = new_fireballs


# Solution function
def solution():
    for _ in range(K):
        move_fireballs()
        sum_fireballs()

    answer = sum(f.massive for f in fireballs)
    print(answer)


# Main function
def main():
    input_data()
    solution()


if __name__ == "__main__":
    main()
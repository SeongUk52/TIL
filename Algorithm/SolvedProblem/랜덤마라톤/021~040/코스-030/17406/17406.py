import itertools
import copy

def rotate_matrix(matrix, r, c, s):
    r, c = r - 1, c - 1  # 0-based index
    for layer in range(1, s + 1):
        # 위쪽
        top = matrix[r - layer][c + layer]
        for col in range(c + layer, c - layer, -1):
            matrix[r - layer][col] = matrix[r - layer][col - 1]

        # 오른쪽
        right = matrix[r + layer][c + layer]
        for row in range(r + layer, r - layer, -1):
            matrix[row][c + layer] = matrix[row - 1][c + layer]
        matrix[r - layer + 1][c + layer] = top

        # 아래쪽
        bottom = matrix[r + layer][c - layer]
        for col in range(c - layer, c + layer):
            matrix[r + layer][col] = matrix[r + layer][col + 1]
        matrix[r + layer][c + layer - 1] = right

        # 왼쪽
        for row in range(r - layer, r + layer):
            matrix[row][c - layer] = matrix[row + 1][c - layer]
        matrix[r + layer - 1][c - layer] = bottom

def calculate_min_sum(matrix, operations):
    min_value = float('inf')
    for perm in itertools.permutations(operations):
        temp_matrix = copy.deepcopy(matrix)
        for r, c, s in perm:
            rotate_matrix(temp_matrix, r, c, s)
        min_value = min(min_value, min(sum(row) for row in temp_matrix))
    return min_value

def main():
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    operations = [tuple(map(int, input().split())) for _ in range(K)]

    result = calculate_min_sum(matrix, operations)
    print(result)

if __name__ == "__main__":
    main()
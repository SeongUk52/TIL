n = int(input())

for _ in range(n):
    left_car = 0
    m = int(input())

    arr_left = list(map(int, input().split()))
    arr_right = set(map(int, input().split()))

    for i in range(m - 1):
        for j in range(i + 1, m):
            if arr_left[i] + 500 == arr_left[j] and arr_left[j] + 500 in arr_right:
                left_car += 1

    print(left_car)
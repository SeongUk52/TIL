n = int(input())


def Hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
        return

    Hanoi(n - 1, a, c, b)
    print(a, c)
    Hanoi(n - 1, b, a, c)


print(2 ** n - 1)  # 이동 횟수
if n <= 20: Hanoi(n, 1, 2, 3)

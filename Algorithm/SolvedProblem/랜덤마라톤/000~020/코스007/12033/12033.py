for tc in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    i = 0
    while n > 0:
        origin = p[i] * (4 / 3)
        if origin in p:
            p.remove(origin)
            n -= 1
        i += 1

    print("Case #" + str(tc + 1), end=": ")
    print(*p)

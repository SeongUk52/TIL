for _ in range(int(input())):
    r, b, m = map(float, input().split())
    cnt = 0
    pb = b
    r = (r + 100.0) / 100.0
    imp = False
    while cnt <= 1200 and not imp:
        cnt += 1
        b = (int((b * r * 100) + 0.5 + 1e-8) / 100.0) - m
        if b <= 0:
            break
        if b > pb:
            imp = True
    if imp or cnt > 1200:
        print("impossible")
    else:
        print(cnt)

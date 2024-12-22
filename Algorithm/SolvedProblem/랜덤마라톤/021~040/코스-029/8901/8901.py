for _ in range(int(input())):
    a, b, c = map(int, input().split())
    abP, bcP, caP = map(int, input().split())
    max_price = 0
    for ab_num in range(min(a, b) + 1):
        max_price = max(
            max_price,
            ab_num * abP + min(b - ab_num, c) * bcP + min(c - min(b - ab_num, c), a - ab_num) * caP,
            ab_num * abP + min(c, a - ab_num) * caP + min(b - ab_num, c - min(c, a - ab_num)) * bcP
        )
    print(max_price)
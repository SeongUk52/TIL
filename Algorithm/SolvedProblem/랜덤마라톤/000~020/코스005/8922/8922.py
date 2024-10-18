tc = int(input())
for _ in range(tc):
    n = int(input())
    tp = list(map(int, input().split()))

    cnt = 0
    while cnt < 1000:
        ntp = [0] * n
        for i in range(n - 1):
            ntp[i] = abs(tp[i] - tp[i + 1])
        ntp[n - 1] = abs(tp[n - 1] - tp[0])
        if ntp == [0] * n:
            break
        else:
            tp = ntp[:]
            cnt += 1

    if cnt < 100:
        print("ZERO")
    else:
        print("LOOP")

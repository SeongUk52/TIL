tc = 0
while True:
    tc += 1
    n = input()
    if n == "0":
        break
    while True:
        if len(n) % 2 == 1:
            break
        pn = ""
        for i in range(0, len(n), 2):
            pn += n[i + 1] * int(n[i])
        if pn == n:
            break
        n = pn
    print("Test " + str(tc) + ": " + n)

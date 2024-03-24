n = input()

if "0" not in n:
    print(-1)

else:
    numSum = 0
    for i in n:
        numSum += int(i)

    if numSum % 3 != 0:
        print(-1)

    else:
        print("".join(sorted(n, reverse=True)))

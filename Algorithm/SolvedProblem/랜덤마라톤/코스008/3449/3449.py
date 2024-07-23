for _ in range(int(input())):
    a = input()
    b = input()
    x = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            x += 1
    print("Hamming distance is %d." % x)

tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = arr[-1]
    result = 0
    for i in range(n - 2, -1, -1):
        ii = arr[i]

        if ii > maxi:
            maxi = ii
        elif ii < maxi:
            result += maxi - ii

    print(result)

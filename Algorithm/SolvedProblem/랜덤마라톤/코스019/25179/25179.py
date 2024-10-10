n, m = map(int, input().split())
if (n - 1) % (m + 1) == 0:
    print("Can't win")
else:
    print("Can win")

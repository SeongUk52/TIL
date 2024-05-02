import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

cnt = 0
dart = []

for i in h:
    if i in dart:
        if i == 1:
            dart.remove(1)
        else:
            dart[dart.index(i)] -= 1

    else:
        dart.append(i - 1)
        cnt += 1


print(cnt)

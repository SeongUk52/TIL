N, M = map(int, input().split())
box = list()
for i in range(N):
    box.append(list(map(int, input().split())))

jocker = list()
one = list()

for b in box:
    already = False
    isOne = -1
    for index in range(M):
        if b[index] != 0:
            if not already:
                already = True
                isOne = index
            else:
                if isOne != -1:
                    jocker.append(b)
                isOne = -1
    if isOne != -1:
        one.append(isOne)

temp = list(set(one))
if len(jocker) == 0:
    if len(one) - len(temp) > 0:
        print(len(one) - len(temp) - 1)
    else:
        print(len(one) - len(temp))
else:
    print(len(jocker) - 1 + len(one) - len(temp))

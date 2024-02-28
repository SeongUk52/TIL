t = int(input())

for i in range(t):
    n = int(input())
    wearDict = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in wearDict:
            wearDict[wear[1]].append(wear[0])
        else:
            wearDict[wear[1]] = [wear[0]]

    cnt = 1

    for k in wearDict:
        cnt *= (len(wearDict[k]) + 1)
    print(cnt-1)

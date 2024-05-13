import sys
input = sys.stdin.readline


def move(ll, dir):
    maxi = 0
    if dir == 0:
        for i in range(n):
            j = 1
            while j < n:
                if ll[i][j] == 0:
                    for k in range(j + 1, n):
                        if ll[i][k] != 0:
                            ll[i][j] = ll[i][k]
                            ll[i][k] = 0
                            break
                if ll[i][j - 1] == ll[i][j]:
                    ll[i][j - 1] *= 2
                    if ll[i][j - 1] > maxi:
                        maxi = ll[i][j - 1]
                    ll[i][j] = 0
                if ll[i][j - 1] == 0 and ll[i][j] != 0:
                    ll[i][j - 1] = ll[i][j]
                    ll[i][j] = 0
                    j -= 1
                j += 1

    elif dir == 1:
        for i in range(n):
            j = n - 2
            while j >= 0:
                if ll[i][j] == 0:
                    for k in range(j - 1, - 1, - 1):
                        if ll[i][k] != 0:
                            ll[i][j] = ll[i][k]
                            ll[i][k] = 0
                            break
                if ll[i][j + 1] == ll[i][j]:
                    ll[i][j + 1] *= 2
                    if ll[i][j + 1] > maxi:
                        maxi = ll[i][j + 1]
                    ll[i][j] = 0
                if ll[i][j + 1] == 0 and ll[i][j] != 0:
                    ll[i][j + 1] = ll[i][j]
                    ll[i][j] = 0
                    j += 1
                j -= 1

    elif dir == 2:
        for j in range(n):
            i = 1
            while i < n:
                if ll[i][j] == 0:
                    for k in range(i + 1, n):
                        if ll[k][j] != 0:
                            ll[i][j] = ll[k][j]
                            ll[k][j] = 0
                            break
                if ll[i - 1][j] == ll[i][j]:
                    ll[i - 1][j] *= 2
                    if ll[i - 1][j] > maxi:
                        maxi = ll[i - 1][j]
                    ll[i][j] = 0
                if ll[i - 1][j] == 0 and ll[i][j] != 0:
                    ll[i - 1][j] = ll[i][j]
                    ll[i][j] = 0
                    i -= 1
                i += 1

    elif dir == 3:
        for j in range(n):
            i = n - 2
            while i >= 0:
                if ll[i][j] == 0:
                    for k in range(i - 1, - 1, - 1):
                        if ll[k][j] != 0:
                            ll[i][j] = ll[k][j]
                            ll[k][j] = 0
                            break
                if ll[i + 1][j] == ll[i][j]:
                    ll[i + 1][j] *= 2
                    if ll[i + 1][j] > maxi:
                        maxi = ll[i + 1][j]
                    ll[i][j] = 0
                if ll[i + 1][j] == 0 and ll[i][j] != 0:
                    ll[i + 1][j] = ll[i][j]
                    ll[i][j] = 0
                    i += 1
                i -= 1
    return ll, maxi


def bt(comb):
    if len(comb) == 5:
        result.append(comb[:])
        return

    for i in range(4):
        comb.append(i)
        bt(comb)
        comb.pop()


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = graph[:]
result = []
bt([])
maxV = 0
for i in result:
    ll = [graph[j][:] for j in range(n)]
    for j in i:
        ll, maxtemp = move(ll, j)
        if maxtemp >= maxV:
            maxV = maxtemp

print(maxV)

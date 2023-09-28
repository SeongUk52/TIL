def bt(comb):
    if len(comb) == k:
        integer = ""
        for i in comb:
            integer += str(cards[i])
        if integer not in result:
            result.append(integer)
        return
    for i in range(n):
        if i not in comb:
            comb.append(i)
            bt(comb)
            comb.pop()


n = int(input())
k = int(input())
cards = [int(input()) for i in range(n)]
result = []
bt([])
print(len(result))
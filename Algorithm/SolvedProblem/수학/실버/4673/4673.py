isSelf = [True] * 10001

def notSelf(para):
    newN = para + sum(map(int, str(para)))
    if newN > 10000:
        return
    isSelf[newN] = False
    notSelf(newN)


n = 1
for i in range(1, 10001):
    if isSelf[i]:
        notSelf(i)

for i in range(1, 10001):
    if isSelf[i]:
        print(i)

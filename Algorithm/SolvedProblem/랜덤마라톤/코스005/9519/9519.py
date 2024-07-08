x = int(input())
results = [list(input())]
while x > 0:
    x -= 1
    flag = True
    left = []
    right = []
    for i in results[-1]:
        if flag:
            left += i
            flag = False
        else:
            right += i
            flag = True
    right.reverse()
    word = left + right
    if word == results[-1]:
        x = 0
        break
    if word in results:
        first = results.index(word)
        now = len(results)
        length = now - first
        x = x % length + first + 1
        break

    results.append(word)

print("".join(results[x - 1]))

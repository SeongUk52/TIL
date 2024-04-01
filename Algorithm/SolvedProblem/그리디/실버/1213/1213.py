from collections import Counter

strs = input()
counter = Counter()
oddCheck = 0
oddWord = ""

for i in strs:
    counter[i] += 1

for i, j in counter.items():
    if j % 2 == 1:
        oddCheck += 1
        oddWord = i
        if oddCheck >= 2:
            break

if oddCheck >= 2:
    print("I'm Sorry Hansoo")

if oddCheck < 2:
    for i, j in sorted(counter.items()):
        for _ in range(j // 2):
            print(i, end="")
    if oddCheck == 1:
        print(oddWord, end="")
    for i, j in sorted(counter.items(), reverse=True):
        for _ in range(j // 2):
            print(i, end="")

import sys

mini = -1_000_000_000_000_000_000
maxi = 1_000_000_000_000_000_000
answer = 0
for i in range(int(input())):
    x, oper = sys.stdin.readline().rstrip().split()
    x = int(x)

    if oper == '^':
        mini = max(mini, x + 1)
    elif oper == 'v':
        maxi = min(maxi, x - 1)

    if mini == maxi and answer == 0:
        answer = i + 1

    if mini > maxi:
        print("Paradox!")
        print(i + 1)
        break

if maxi > mini:
    print("Hmm...")

if maxi == mini:
    print("I got it!")
    print(answer)

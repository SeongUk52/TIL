import sys

yeondu = input()
t = int(input())
teams = [sys.stdin.readline().rstrip() for _ in range(t)]

teams.sort()
ans = ""
maximum = -1

for team in teams:
    word = yeondu + team
    L, O, V, E = word.count('L'), word.count('O'), word.count('V'), word.count('E')
    total = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

    if total > maximum:
        ans = team
        maximum = total

print(ans)
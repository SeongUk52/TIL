import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon = {}

for i in range(1, n + 1):
    a = input().rstrip()
    pokemon[i] = a
    pokemon[a] = i

for _ in range(m):
    inp = input().rstrip()
    if inp.isdigit():
        print(pokemon[int(inp)])
    else:
        print(pokemon[inp])

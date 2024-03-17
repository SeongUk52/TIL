import sys
s = sys.stdin.readline().rstrip()
ppap = []
ans = 'NP'
for i in s:
    ppap.append(i)
    if len(ppap) >= 4 and ppap[-4:] == ['P', 'P', 'A', 'P']:
        for _ in range(3):
            ppap.pop()
if len(ppap) == 1 and ppap[0] == 'P':
    ans = 'PPAP'
print(ans)

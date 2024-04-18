s = input()
t = input()
diff = len(t) - len(s)
for i in range(diff):
    if t[-1] == 'A':
        t = t[0:-1]
    else:
        t = t[0:-1]
        t = t[::-1]
if s == t:
    print(1)
else:
    print(0)

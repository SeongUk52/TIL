x = input()
apls = True
degree = int(x[1]) - int(x[0])
if degree <= 0:
    apls = False

for i in range(1, len(x)):
    nDeg = int(x[i]) - int(x[i - 1])
    if nDeg == 0:
        apls = False
        break
    if 0 < nDeg * degree and nDeg != degree:
        apls = False
        break
    degree = nDeg

if degree >= 0:
    apls = False

if apls:
    print("ALPSOO")
else:
    print("NON ALPSOO")

ll = input()
ph, pg = 0, 0
for i in ll:
    if i in "HAPPY":
        ph += 1
    if i in "SAD":
        pg += 1
if ph == pg == 0:
    result = 50.00
else:
    result = int(10000 * ph / (ph + pg) + 0.5) / 100
print("{:.2f}".format(result))

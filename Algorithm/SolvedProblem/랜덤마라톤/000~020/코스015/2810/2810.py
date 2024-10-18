n = int(input())
mem = input()
cnt = mem.count("LL")
if cnt <= 1:
    print(len(mem))
else:
    print(len(mem) - cnt + 1)

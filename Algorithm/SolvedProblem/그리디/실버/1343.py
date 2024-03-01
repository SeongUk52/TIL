ll = input()
ll = ll.replace("XXXX", "AAAA")
ll = ll.replace("XX", "BB")

if 'X' in ll:
    print(-1)
else:
    print(ll)

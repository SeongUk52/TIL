import heapq
for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    nl = list(map(int, input().split()))
    ml = list(map(int, input().split()))
    heapq.heapify(nl)
    heapq.heapify(ml)
    while len(nl) + len(ml) > 1 and nl and ml:
        nn = heapq.heappop(nl)
        mm = heapq.heappop(ml)
        if nn >= mm:
            heapq.heappush(nl, nn)
        else:
            heapq.heappush(ml, mm)
    if len(nl) > len(ml):
        print("S")
    elif len(ml) > len(nl):
        print("B")
    else:
        print("C")

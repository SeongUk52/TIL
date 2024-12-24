import sys
from bisect import bisect_left
input = sys.stdin.readline

while True:
    try:
        N = int(input())
        prices = list(map(int, input().split()))
        array = [prices[0]]

        for i in range(1, N):
            idx = bisect_left(array, prices[i])
            if idx == len(array):
                array.append(prices[i])
            else:
                array[idx] = prices[i]

        print(len(array))
    except:
        break
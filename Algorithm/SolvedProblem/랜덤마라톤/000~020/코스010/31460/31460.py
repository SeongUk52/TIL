print(*[[0, '1' + '2' * (int(i) - 2) + '1'][int(i) > 1] for i in open(0)][1:])

from collections import defaultdict


def main():
    import sys
    input = sys.stdin.read

    data = input().split()
    n, m, slen = map(int, data[:3])
    grid = data[3:3 + n]
    s = data[3 + n]

    # Store positions of each character in a defaultdict
    v = defaultdict(list)
    for i in range(n):
        for j in range(m):
            v[grid[i][j]].append((i, j))

    # Count the occurrences of each character in string s
    cnt = defaultdict(int)
    for char in s:
        cnt[char] += 1

    # Calculate maximum number of times we can build the string
    ansC = float('inf')
    for char in s:
        ansC = min(ansC, len(v[char]) // cnt[char])

    # Prepare movement directions
    l = []

    def move(cur, target):
        nonlocal l
        dr = target[0] - cur[0]
        dc = target[1] - cur[1]

        rc = 'D' if dr > 0 else 'U'
        cc = 'R' if dc > 0 else 'L'

        l.extend([rc] * abs(dr))
        l.extend([cc] * abs(dc))

    cur = (0, 0)

    for _ in range(ansC):
        for char in s:
            target = v[char].pop()
            move(cur, target)
            l.append('P')  # Pick up the letter
            cur = target

    # Move to the bottom-right corner of the grid
    move(cur, (n - 1, m - 1))

    # Output results
    print(ansC, len(l))
    print(''.join(l))


if __name__ == "__main__":
    main()

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        people = list(input().strip())

        # 사람 수 카운트와 마지막 인덱스 저장
        people_cnt = {}
        last_idx = {}

        for i in range(N):
            person = people[i]
            if person not in people_cnt:
                people_cnt[person] = 0
            people_cnt[person] += 1
            last_idx[person] = i

        # 그룹 생성
        groups = [Group(name, last_idx[name]) for name in people]

        # 마지막 인덱스 기준 정렬
        groups.sort()

        ans = 0
        i = 0
        while i < N:
            current = groups[i].name
            group_cnt = people_cnt[current]

            last_group_idx = i + group_cnt - 1
            ans += 5 * (last_idx[current] - last_group_idx) * group_cnt

            i = last_group_idx + 1

        print(ans)


class Group:
    def __init__(self, name, last_index):
        self.name = name
        self.last_index = last_index

    def __lt__(self, other):
        return self.last_index < other.last_index


if __name__ == "__main__":
    main()
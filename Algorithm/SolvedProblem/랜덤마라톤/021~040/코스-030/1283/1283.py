n = int(input())

exist = set()
for _ in range(n):
    words = input().split()
    flag = False

    # 첫 글자로 단축키 지정
    for i, word in enumerate(words):
        if word[0].upper() not in exist:
            exist.add(word[0].upper())
            words[i] = f'[{word[0]}]{word[1:]}'
            print(' '.join(words))
            flag = True
            break

    # 첫 글자가 사용 불가능한 경우
    if not flag:
        for i, word in enumerate(words):
            for j, char in enumerate(word):
                if char.upper() not in exist:
                    exist.add(char.upper())
                    words[i] = f'{word[:j]}[{char}]{word[j+1:]}'
                    print(' '.join(words))
                    flag = True
                    break
            if flag:
                break

    # 어떤 경우에도 단축키를 지정할 수 없는 경우
    if not flag:
        print(' '.join(words))
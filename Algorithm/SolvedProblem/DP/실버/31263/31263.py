N = int(input())
lst = list(map(str, input().strip()))

ans = 0

while lst:
    if len(lst) <= 3:  # 남은 자릿수가 3 이하일 때
        if int(''.join(lst)) <= 641:
            ans += 1
            break
        else:
            lst = lst[2:]  # 2자리로 처리
            ans += 1
    else:  # 남은 자릿수가 4 이상일 때
        if lst[2] == '0':  # 세 번째 자리가 '0'
            if len(lst) > 3 and lst[3] == '0':  # 네 번째 자리도 '0'
                lst = lst[1:]  # 한 자리 처리
                ans += 1
            elif int(''.join(lst[:3])) <= 641:  # 세 자리 숫자가 유효
                lst = lst[3:]  # 3자리 처리
                ans += 1
            else:  # 유효하지 않으면 한 자리 처리
                lst = lst[1:]
                ans += 1
        else:  # 세 번째 자리가 '0'이 아닐 때
            if len(lst) > 3 and lst[3] == '0':  # 네 번째 자리가 '0'
                lst = lst[2:]  # 2자리 처리
                ans += 1
            elif int(''.join(lst[:3])) <= 641:  # 세 자리 숫자가 유효
                lst = lst[3:]  # 3자리 처리
                ans += 1
            else:  # 유효하지 않으면 2자리 처리
                lst = lst[2:]
                ans += 1

print(ans)
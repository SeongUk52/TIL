def main():
    nato = [
        "aespa", "baekjoon", "cau", "debug",
        "edge", "firefox", "golang", "haegang",
        "iu", "java", "kotlin", "lol", "mips",
        "null", "os", "python", "query", "roka",
        "solvedac", "tod", "unix", "virus", "whale",
        "xcode", "yahoo", "zebra"
    ]

    str_input = input()
    able = True
    curr = 0
    ans = ""

    while curr < len(str_input):
        idx = ord(str_input[curr]) - ord('a')

        if idx < 0 or idx >= len(nato):
            able = False
            break

        sz = len(nato[idx])

        if sz > len(str_input) - curr:
            able = False
            break

        tmp = str_input[curr:curr + sz]
        if tmp == nato[idx]:
            curr += sz
            ans += chr(idx + ord('a'))
        else:
            able = False
            break

    if able:
        print("It's HG!")
        print(ans)
    else:
        print("ERROR!")

if __name__ == "__main__":
    main()
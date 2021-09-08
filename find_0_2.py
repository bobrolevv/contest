# id 52782682

def find_zero(hooms_numb: str, len_street: str) -> str:
    len_street: int = int(len_street)
    res: int = [len_street] * len_street
    position: int = 1

    flag: bool = False
    for up in range(0, len_street):
        if hooms_numb[up] == 0:
            position = 0
            flag = True

        if flag: res[up] = position
        position += 1

    for down in range(len_street-1, -1, -1):
        if hooms_numb[down] == 0:
            position = 0
        if res[down] > position: res[down] = position
        position += 1

    return (" ".join(map(str, res)))

def main():
    len_street = input()
    hooms_numb = list(map(int, input().split()))
    print(find_zero(hooms_numb, len_street))

if __name__ == '__main__':
    main()

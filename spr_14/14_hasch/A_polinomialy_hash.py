a = int(input())                        # основание
m = int(input())                        # модуль
# s = [ord(x) for x in input()]
# s = list(map(ord, input()))
s = input()                             # строка
n = len(s)                              # длинна строки

def find_hash(a: int, m: int, s: str) -> int:
    res = 0
    k = 1
    for i in s:
        res += (ord(i) * a**(n-k))
        k += 1

    return res % m

DIC = 'abcdefghijklmnopqrstuwvxyz'

def duble_hash(hash, my_dict):
    if hash == find_hash(a, m, s):
        return hash
    else:
        for i in DIC:
            duble_hash()


if __name__ == '__main__':
    print(find_hash(a, m, s))
